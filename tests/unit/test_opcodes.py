import unittest
from circuitroomba.series6 import opcode


class Test_opcode_are_set_correct(unittest.TestCase):
    """
    Validating hex codes set in opcode translate to the correct byte codes
    found on page 33 of the Roomba Open Interface Spec
    """

    def test_start(self):
        self.assertEqual(opcode.START, hex(128))

    def test_baud_rate(self):
        self.assertEqual(opcode.BAUD, hex(129))

    def test_control(self):
        self.assertEqual(opcode.CONTROL, hex(130))

    def test_safe(self):
        self.assertEqual(opcode.SAFE, hex(131))

    def test_full(self):
        self.assertEqual(opcode.FULL, hex(132))

    def test_power(self):
        self.assertEqual(opcode.POWER, hex(133))

    def test_spot(self):
        self.assertEqual(opcode.SPOT, hex(134))

    def test_clean(self):
        self.assertEqual(opcode.CLEAN, hex(135))

    def test_max_clean(self):
        self.assertEqual(opcode.MAX_CLEAN, hex(136))

    def test_drive(self):
        self.assertEqual(opcode.DRIVE, hex(137))

    def test_motors(self):
        self.assertEqual(opcode.MOTORS, hex(138))

    def test_pwm_moros(self):
        self.assertEqual(opcode.PWM_MOTORS, hex(144))

    def test_drive_pwm(self):
        self.assertEqual(opcode.DRIVE_PWM, hex(146))

    def test_leds(self):
        self.assertEqual(opcode.LEDS, hex(139))

    def test_song(self):
        self.assertEqual(opcode.SONG, hex(140))

    def test_play(self):
        self.assertEqual(opcode.PLAY, hex(141))

    def test_stream(self):
        self.assertEqual(opcode.STREAM, hex(148))

    def test_query_list(self):
        self.assertEqual(opcode.QUERY_LIST, hex(149))

    def test_do_stream(self):
        self.assertEqual(opcode.DO_STREAM, hex(150))

    def test_query(self):
        self.assertEqual(opcode.QUERY, hex(142))

    def test_force_seeking_doc(self):
        self.assertEqual(opcode.FORCE_SEEKING_DOCK, hex(143))

    def test_scheduling_leds(self):
        self.assertEqual(opcode.SCHEDULING_LEDS, hex(162))

    def test_digit_leds_raw(self):
        self.assertEqual(opcode.DIGIT_LEDS_RAW, hex(163))

    def test_digit_leds_ascii(self):
        self.assertEqual(opcode.DIGIT_LEDS_ASCII, hex(164))

    def test_buttons(self):
        self.assertEqual(opcode.BUTTONS, hex(165))

    def test_schedule(self):
        self.assertEqual(opcode.SCHEDULE, hex(167))

    def test_set_day_time(self):
        self.assertEqual(opcode.SET_DAY_TIME, hex(168))

    def test_stop(self):
        self.assertEqual(opcode.STOP, hex(173))
