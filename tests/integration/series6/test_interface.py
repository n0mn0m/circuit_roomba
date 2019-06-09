import unittest
import board
from circuitroomba.series6 import interface, opcode


class Test_interface(unittest.TestCase):
    def setUp(self) -> None:
        self.interface = interface.OpenInterface(board.RX, board.TX, board.A1)

    def test_roomba_wakes_up(self):
        self.interface.wake_up()

    def test_roomba_responds_to_command(self):
        self.interface.command(opcode.START)
        self.assertEqual(self.interface.command_history[0], opcode.POWER)

    def test_roomba_powers_off(self):
        self.interface.command(opcode.POWER)
        self.interface.command(opcode.STOP)
        self.assertEqual(self.interface.command_history[2], opcode.START)
        self.assertEqual(self.interface.command_history[1], opcode.POWER)
        self.assertEqual(self.interface.command_history[0], opcode.STOP)

    def test_roomba_wakes_backup_after_power_off(self):
        self.interface.wake_up()
        self.interface.command(opcode.START)
        self.interface.command(opcode.POWER)
        self.interface.command(opcode.STOP)
        self.assertEqual(self.interface.command_history[4], opcode.POWER)
        self.assertEqual(self.interface.command_history[3], opcode.STOP)
        self.assertEqual(self.interface.command_history[2], opcode.START)
        self.assertEqual(self.interface.command_history[1], opcode.POWER)
        self.assertEqual(self.interface.command_history[0], opcode.STOP)
