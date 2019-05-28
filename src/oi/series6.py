import digitalio
import time
from .opcodes import *

class RoombaController:
    def __init__:

    """
    This class maps the pins on your board (where Circuit Python is executing) to the Roomba Open Interface
    and exposes a set of helper methods.


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
    By default, Roomba communicates at 115200 baud. If you are using a microcontroller that does not
    support 115200 baud, there are two ways to force Roomba to switch to 19200:

    Method 1:
    While powering off Roomba, continue to hold down the Clean/Power button after the light has turned off.
    After about 10 seconds, Roomba plays a tune of descending pitches. Roomba will communicate at 19200 baud
    until the processor loses battery power or the baud rate is explicitly changed by way of the OI.

    Method 2:
    Use the Baud Rate Change pin (pin 5 on the Mini-DIN connector) to change Roomba’s baud rate.
    After turning on Roomba, wait 2 seconds and then pulse the Baud Rate Change low three times.
    Each pulse should last between 50 and 500 milliseconds. Roomba will communicate at 19200 baud until the
    processor loses battery power or the baud rate is explicitly changed by way of the OI.
    """

    def __init__(self, input_pin, output_pin, baud_rate_change_pin):
        self.rx_pin = input_pin
        self.tx_pin = output_pin
        self.brc_pin = baud_rate_change_pin

    def __repr__(self):
        return "Roomba pin mapping\nRX PIN: %s\nTX PIN %s\nBAUD RATE CHANGE PIN %s\n", self.rx_pin, self.tx_pin, self.brc_pin

    def set_baud_rate(self, baud_rate=19200):
        """
        Function should be the first call after the roomba is powered on
        to set new BRC. This is not required if your boards baud rate is
        115200.

        See page 4 of the Open Interface Create 2/Series 6 manual.
        """
        time.sleep(2)
        self.brc_pin.direction = digitalio.Direction.OUTPUT
        for i in range(3):
            self.brc_pin.value = False
            time.sleep(.25)
            self.brc_pin.value = True

    def wake_up(self):
        self.pin_five.direction = digitalio.Direction.OUTPUT
        self.pin_five.value = False
        time.sleep(.5)
        self.pin_five.value = True
        time.sleep(.5)
        self.pin_five.value = False

    def go(self):
        self.pin_three.value = START
        self.pin_three.value = SAFE
        self.pin_three.value = CLEAN

    def stop(self):
        self.pin_three.value = POWER
        self.pin_three.value = STOP
