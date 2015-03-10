import unittest
from ChessBoard import ChessBoard


class LucyTests(unittest.TestCase):

    def setUp(self):
        self.cb = ChessBoard()

    def testThatTheBlackPAwnMovesForward1Or2Steps(self):
        valid_moves = self.cb.get_valid_moves((0, 6)) # The first black pawn
        assert valid_moves[0] == (0, 5)
        assert valid_moves[1] == (0, 4)
        valid_moves = self.cb.get_valid_moves((1, 6))
        assert  valid_moves[0] == (1, 5)
        assert  valid_moves[1] == (1, 4)

    def testBlackFirstMove(self):
        valid_moves = self.cb.get_valid_moves((4, 6)) # The first black pawn
        assert valid_moves[0] == (4, 5)
        assert valid_moves[1] == (4, 4)


    def testWhiteFirstMove(self):
        self.cb.add_text_move('e2e4')
        valid_moves = self.cb.get_valid_moves((5, 1)) # The first white pawn
        assert valid_moves[0] == (5, 2)
        assert valid_moves[1] == (5, 3)

    def test4eCanEat5f(self):
        self.cb.add_text_move('e2e4')
        self.cb.add_text_move('f7f5')
        valid_moves = self.cb.get_valid_moves((4, 4)) # The black
        assert valid_moves[0] == (4, 3)
        assert valid_moves[1] == (5, 3)

    def testWhiteSecondMove(self):
        self.cb.add_text_move('e2e4')
        self.cb.add_text_move('f7f5')
        self.cb.add_text_move('e4f5')
        valid_moves = self.cb.get_valid_moves((6, 0)) # The white
        assert valid_moves[0] == (7, 2)
        assert valid_moves[1] == (5, 2)

    def testBlackThirdMove(self):
        self.cb.add_text_move('e2e4')
        self.cb.add_text_move('f7f5')
        self.cb.add_text_move('e4f5')
        self.cb.add_text_move('g8h6')
        valid_moves = self.cb.get_valid_moves((5, 7)) # The black
        assert valid_moves[0] == (4, 6)
        assert valid_moves[1] == (3, 5)
        assert valid_moves[2] == (2, 4)
        assert valid_moves[3] == (1, 3)
        assert valid_moves[4] == (0, 2)

    def testWhiteFourthMove(self):
        self.cb.add_text_move('e2e4')
        self.cb.add_text_move('f7f5')
        self.cb.add_text_move('e4f5')
        self.cb.add_text_move('g8h6')
        self.cb.add_text_move('f1d3')
        valid_moves = self.cb.get_valid_moves((7, 2)) # The white
        assert valid_moves[0] == (6, 4)
        assert valid_moves[1] == (5, 3)
        assert valid_moves[2] == (6, 0)
        assert valid_moves[3] == (5, 1)

    def testBlackFourthMove(self):
        self.cb.add_text_move('e2e4')
        self.cb.add_text_move('f7f5')
        self.cb.add_text_move('e4f5')
        self.cb.add_text_move('g8h6')
        self.cb.add_text_move('f1d3')
        self.cb.add_text_move(('h6f5'))
        valid_moves = self.cb.get_valid_moves((3, 5)) # The black
        assert valid_moves[0] == (4, 6)
        assert valid_moves[1] == (5, 7)
        assert valid_moves[2] == (4, 4)
        assert valid_moves[3] == (5, 3)
        assert valid_moves[4] == (2, 4)
        assert valid_moves[5] == (1, 3)
        assert valid_moves[6] == (0, 2)
