import unittest
from ChessBoard import ChessBoard


class LucyTests(unittest.TestCase):

    def setUp(self):
        self.cb = ChessBoard()

    def testThatTheBlackPAwnMovesForward1Or2Steps(self):
        valid_moves = self.cb.getValidMoves((0, 6)) # The first black pawn
        assert valid_moves[0] == (0, 5)
        assert valid_moves[1] == (0, 4)

