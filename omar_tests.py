import unittest
from ChessBoard import ChessBoard


class OmarTests(unittest.TestCase):

    def setUp(self):
        self.cb = ChessBoard()

    def testThatFirstTurnIsWhite(self):
        assert self.cb.getTurn() == self.cb.WHITE

    def testThatAfterWhiteMoveTheTurnIsBlack(self):
        self.cb.add_text_move('e2e4')
        assert self.cb.getTurn() == self.cb.BLACK