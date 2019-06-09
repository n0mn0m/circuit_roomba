import unittest
import board
from circuitroomba.series6 import roomba


class Test_roomba_commands(unittest.TestCase):
    def setUp(self) -> None:
        self.roomba = roomba.Roomba(board.RX, board.TX, board.A1, 19200)

    def test_roomba_sets_baud_rate_to_19200(self):
        self.roomba.wake_up()
        self.roomba.set_baud_rate_19200()
        self.roomba.start()
        self.roomba.clean()
        self.roomba.stop()
        self.assertEqual(self.roomba.baud_rate, 19200)
