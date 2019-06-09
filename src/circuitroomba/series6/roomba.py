import time
from .opcode import START, STOP, CLEAN, RESET, BAUD, baud_codes
from .interface import OpenInterface


class Roomba(OpenInterface):
    """
    """

    def __init__(self, rx_pin, tx_pin, brc_pin, baud_rate=115200):
        super().__init__(rx_pin, tx_pin, brc_pin, baud_rate)

    def __repr__(self):
        return (
            "Roomba pin mapping\nRX PIN: %s\nTX PIN %s\nBAUD RATE CHANGE PIN %s\n",
            self._rx_pin,
            self._tx_pin,
            self._brc_pin,
        )

    def start(self):
        """
        This command starts the OI.

        You must always send the Start command before sending any other commands
        to the OI.

        - Serial sequence: [128].
        - Available in modes: Passive, Safe, or Full
        - Changes mode to: Passive. Roomba beeps once to acknowledge it is starting
          from “off” mode.
        """

        self.command(START)

    def clean(self):
        self.command(CLEAN)

    def stop(self):
        """
        This command stops the OI. All streams will stop and the robot will no
        longer respond to commands. Use this command when you are finished working
        with the robot.

        - Serial sequence: [173].
        - Available in modes: Passive, Safe, or Full
        - Changes mode to: Off. Roomba plays a song to acknowledge it is exiting the OI.
        """
        self.command(STOP)

    def reset(self):
        """
        This command resets the robot, as if you had removed and reinserted the battery.

        - Serial sequence: [7].
        - Available in modes: Always available.
        - Changes mode to: Off. You will have to send start again to re-enter Open
          Interface mode.
        """

        self.command(RESET)

    def set_baud_rate_19200(self):
        """
        By default the Roomba Open Interface listens for commands at baud rate 115200.
        If you have a controller that needs to use 19200 on serial instead this method
        should be called right after the Roomba wakes up before any other commands.
        """
        self._brc_set_baud_rate()

    def baud(self, baud_rate_code=None):
        """
        This command sets the baud rate in bits per second (bps) at which OI commands
        and data are sent according to the baud code sent in the data byte. The default
        baud rate at power up is 115200 bps, but the starting baud rate can be changed
        to 19200 by following the method outlined on page 4. Once the baud rate is
        changed, it persists until Roomba is power cycled by pressing the power button
        or removing the battery, or when the battery voltage falls below the minimum
        required for processor operation. You must wait 100ms after sending this command
        before sending additional commands at the new baud rate.

        - Serial sequence: [129][Baud Code]
        - Available in modes: Passive, Safe, or Full
        - Changes mode to: No Change
        - Baud data byte 1: Baud Code (0 - 11)
        """

        if baud_rate_code in baud_codes.keys():
            self.baud_rate = baud_codes[baud_rate_code]
            self.command(BAUD, baud_rate_code)
            # per the OI spec another command cannot be issued after the baud command
            # for 100ms
            time.sleep(1 / 1000000)
        else:
            raise RuntimeError(
                "Invalid baud rate code. Please refer to page 9 of the"
                "Roomba Open Interface Spec."
            )
