import unittest
from ChessBoard import ChessBoard

class MyChessBoard(ChessBoard):
    def add_move(self, fromPos, toPos):
        self.called_from_pos = fromPos
        self.called_to_pos = toPos

class CagriTests(unittest.TestCase):

    def setUp(self):
        self.cb = MyChessBoard()

    # Check if the (0,0) and (0,7) is movable
    def testThatA1A8Movable(self):
        self.cb.add_text_move('a1a8')
        assert self.cb.called_from_pos == (0,7)
        assert self.cb.called_to_pos == (0,0)

    # Check if 'a0a9' is not movable (out of bounds)
    def testThatA0A9NotMovable(self):
        assert self.cb.add_text_move('a0a9') == False

    # Check if 'a1a9' is not movable (out of bounds)
    def testThatA1A9NotMovable(self):
        assert self.cb.add_text_move('a1a9') == False

    # Check if the (7,0) and (7,7) is movable
    def testThatH1H8Movable(self):
        self.cb.add_text_move('h1h8')
        assert self.cb.called_from_pos == (7,7)
        assert self.cb.called_to_pos == (7,0)

    # Check if 'h0h9' is not movable (out of bounds)
    def testThatH1H9NotMovable(self):
        assert self.cb.add_text_move('h0h9') == False

    # Check if 'h1h9' is not movable (out of bounds)
    def testThatH1H9NotMovable(self):
        assert self.cb.add_text_move('h1h9') == False

    # Checks if the caps lock commands are not working
    def testThatCapsAreNotWorking(self):
        assert self.cb.add_text_move('A3F5') == False

    # Checks if many moves are working
    # Accepts the last 2 commands
    def testThatManyMovesAreWorking(self):
        self.cb.add_text_move('b7e3d2a5')
        assert self.cb.called_from_pos == (3,6)
        assert self.cb.called_to_pos == (0,3)

    # Tests below this line checks if the moves defined in the main are valid moves.
    def testThatE2E4Movable(self):
        self.cb.add_text_move('e2e4')
        assert self.cb.called_from_pos == (4,6)
        assert self.cb.called_to_pos == (4,4)

    def testThatF7F5Movable(self):
        self.cb.add_text_move('f7f5')
        assert self.cb.called_from_pos == (5,1)
        assert self.cb.called_to_pos == (5,3)

    def testThatE4F5Movable(self):
        self.cb.add_text_move('e4f5')
        assert self.cb.called_from_pos == (4,4)
        assert self.cb.called_to_pos == (5,3)

    def testThatG8H6Movable(self):
        self.cb.add_text_move('g8h6')
        assert self.cb.called_from_pos == (6,0)
        assert self.cb.called_to_pos == (7,2)

    def testThatF1D3Movable(self):
        self.cb.add_text_move('f1d3')
        assert self.cb.called_from_pos == (5,7)
        assert self.cb.called_to_pos == (3,5)

    def testThatH6F5Movable(self):
        self.cb.add_text_move('h6f5')
        assert self.cb.called_from_pos == (7,2)
        assert self.cb.called_to_pos == (5,3)

    def testThatD3F5Movable(self):
        self.cb.add_text_move('d3f5')
        assert self.cb.called_from_pos == (3,5)
        assert self.cb.called_to_pos == (5,3)