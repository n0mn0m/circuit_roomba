import unittest
import board
from circuitroomba.series6 import roomba


class Test_roomba_commands(unittest.TestCase):
    def test_roomba_sets_baud_rate_to_19200(self):
        bot = roomba.Commands(board.RX, board.TX, board.A1, 19200)
        bot.wake_up()
        bot.set_baud_rate_19200()
        bot.start()
        bot.clean()
        bot.stop()
        self.assertEqual(self.roomba.baud_rate, 19200)
