import unittest
from circuit_roomba import opcodes


class Test_opcodes_are_set_correct(unittest.TestCase):
    """
    Validating hex codes set in opcodes translate to the correct byte codes
    found on page 33 of the Roomba Open Interface Spec
    """

    def test_start(self):
        self.assertEqual(opcodes.START, bytes(128))

    def test_baud_rate(self):
        self.assertEqual(opcodes.START, bytes(129))

    def test_control(self):
        self.assertEqual(opcodes.START, bytes(130))

    def test_safe(self):
        self.assertEqual(opcodes.START, bytes(131))

    def test_full(self):
        self.assertEqual(opcodes.START, bytes(132))

    def test_power(self):
        self.assertEqual(opcodes.START, bytes(133))

    def test_spot(self):
        self.assertEqual(opcodes.START, bytes(134))

    def test_clean(self):
        self.assertEqual(opcodes.START, bytes(135))

    def test_max_clean(self):
        self.assertEqual(opcodes.START, bytes(136))

    def test_drive(self):
        self.assertEqual(opcodes.START, bytes(137))

    def test_motors(self):
        self.assertEqual(opcodes.START, bytes(138))

    def test_pwm_moros(self):
        self.assertEqual(opcodes.START, bytes(144))

    def test_drive_pwm(self):
        self.assertEqual(opcodes.START, bytes(146))

    def test_leds(self):
        self.assertEqual(opcodes.START, bytes(139))

    def test_song(self):
        self.assertEqual(opcodes.START, bytes(140))

    def test_play(self):
        self.assertEqual(opcodes.START, bytes(141))

    def test_stream(self):
        self.assertEqual(opcodes.START, bytes(148))

    def test_query_list(self):
        self.assertEqual(opcodes.START, bytes(149))

    def test_do_stream(self):
        self.assertEqual(opcodes.START, bytes(150))

    def test_query(self):
        self.assertEqual(opcodes.START, bytes(142))

    def test_force_seeking_doc(self):
        self.assertEqual(opcodes.START, bytes(143))

    def test_scheduling_leds(self):
        self.assertEqual(opcodes.START, bytes(162))

    def test_digit_leds_raw(self):
        self.assertEqual(opcodes.START, bytes(163))

    def test_digit_leds_ascii(self):
        self.assertEqual(opcodes.START, bytes(164))

    def test_buttons(self):
        self.assertEqual(opcodes.START, bytes(165))

    def test_schedule(self):
        self.assertEqual(opcodes.START, bytes(167))

    def test_set_day_time(self):
        self.assertEqual(opcodes.START, bytes(168))

    def test_stop(self):
        self.assertEqual(opcodes.START, bytes(173))
