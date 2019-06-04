import time
import digitalio
from .opcode import commands, mode_commands, valid_modes


class OpenInterface:
    """
    This class maps the pins on your board (where Circuit Python is executing) to the
    Roomba Open Interface.

    This class is focused on lower level details of the Open Interface spec while the
    Roomba class exposes higher level help methods and operations.


          6
    7 - . . . - 5
    4 - .   . - 3
     2 - . . - 1


    Pin 1 - Vpwr - Roomba Battery + (unregulated)
    Pin 2 - Vpwr - Roomba Battery + (unregulated)
    Pin 3 - RXD - 0-5V Serial Input to Roomba
    Pin 4 - TXD - 0-5V Serial Output from Rooba
    Pin 5 - BRC - Baud rate change
    Pin 6 - GND - Roomba battery ground
    Pin 7 - GND - Roomba battery ground

    Serial Port Settings
    Baud: 115200 or 19200 (see below) Data bits: 8
    Parity: None
    Stop bits: 1
    Flow control: None

    By default, Roomba communicates at 115200 baud. If you are using a microcontroller
    that does not support 115200 baud, there are two ways to force Roomba to switch to
    19200:

    https://www.irobotweb.com/~/media/MainSite/PDFs/About/STEM/Create/iRobot_Roomba_600_Open_Interface_Spec.pdf # noqa
    """

    def __init__(self, input_pin, output_pin, baud_rate_change_pin, baud_rate=115200):
        """
        Initialize communication pins and state. State is referred to as
        operating mode to stay consistent with the Open Interface Specification
        document.

        Two list are created to capture operating mode and command history. Both
        store the last 5 items processed.
        """
        self._rx_pin = input_pin
        self._tx_pin = output_pin
        self._brc_pin = baud_rate_change_pin
        self.baud_rate = baud_rate
        self.operating_mode = "off"
        self.operating_mode_history = [0 for i in range(4)]
        self.command = None
        self.command_history = [0 for i in range(4)]
        self.data = None
        self.data_history = [0 for i in range(4)]

    @property
    def operating_mode(self):
        return self.operating_mode

    @operating_mode.setter
    def operating_mode(self, new_mode):
        if new_mode not in valid_modes:
            raise RuntimeError(
                "New mode %s is not a valid mode. See page 5 of the open interface"
                "specification or refer to the OpenInterface valid_modes attribute.",
                new_mode,
            )
        else:
            self.mode_history.pop()
            self.mode_history.insert(0, self.operating_mode)
            self.operating_mode = new_mode

    @property
    def valid_modes(self):
        return valid_modes

    @property
    def command(self):
        return self.command

    @command.setter
    def command(self, new_command, data=None):
        """
        Accepts an inbound command that should be sent to the OI RX pin.
        Data should be an int inline with the OI specification document
        that will be handled as bytes internally.

        Command is called to handle validation of the mode and state
        transition as well as verify the data matches spec requirements.
        """
        self.data = bytes(data)
        command_struct = commands[new_command]

        self.command_history.pop()
        self.command_history.insert(0, command_struct["hex_opcode"])
        self.command = command_struct["hex_opcode"]

        if new_command in mode_commands[new_command]:
            self._rx_pin.value = self.command
        else:
            raise RuntimeError(
                "Illegal command in current mode.\nCannot call %s in %s mode.\nRefer"
                "to the Roomba 600 Interface Spec for more information",
                new_command,
                self.operating_mode,
            )

        if (
            command_struct["data_bytes"]
            and len(self.data) == command_struct["data_bytes"]
        ):
            self.data_history.pop()
            self.data_history.insert(0, self.data)
            self._rx_pin.value = self.data
        else:
            raise RuntimeError(
                "Correct amount of data bytes not provided for command.\n"
                "Expected %s "
                "Recieved %s.\n"
                "Refer to command %s in Roomba Open Interface Spec for data byte "
                "information",
                command_struct["data_bytes"],
                len(self.data),
                new_command,
            )

        if command_struct["new_mode"]:
            self.operating_mode = command_struct["new_mode"]
            self._rx_pin = command_struct["new_mode_hex_opcode"]

    @property
    def baud_rate(self):
        return self.baud_rate

    def _manual_set_baud_rate(self, baud_rate=19200):
        """
        Function should be the first call after the circuitroomba is powered on
        to set new BRC. This is not required if your boards baud rate is
        115200.

        For manipulating baud rate after commands have been issued
        use the baud command from the Open Interface spec.

        See page 4 of the Open Interface Create 2/Series 6 manual for
        information on setting the baud rate at startup.
        """
        self._brc_pin.direction = digitalio.Direction.OUTPUT

        for i in range(3):
            self._brc_pin.value = False
            time.sleep(0.25)
            self._brc_pin.value = True
            time.sleep(0.25)

        self.baud_rate = baud_rate

    def keep_awake(self, duty_cycle=60):
        """
        In passive mode the circuitroomba will go into a sleep mode after 5 minutes
        without activity. To prevent this we can pulse the BRC pin low on
        a given duty_cycle.

        Currently need a way to put this into a queue, a background thread,
        async task etc that sleeps for the duty cycle wakes up to pulse the
        brc pin and then goes into the background again.
        """
        raise NotImplementedError
