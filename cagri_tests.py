import unittest
from ChessBoard import ChessBoard

class MyChessBoard(ChessBoard):
    def addMove(self, fromPos, toPos):
        self.called_from_pos = fromPos
        self.called_to_pos = toPos
        print(fromPos)
        print(toPos)
        print("here!!!")

class OmarTests(unittest.TestCase):

    def setUp(self):
        self.cb = MyChessBoard()

    def testThatE2e4Movebla(self):
        self.cb.addTextMove('e2e4')
        assert self.cb.called_from_pos == (4,6)
        assert self.cb.called_to_pos == (4,4)

    def testThatE2e4Movebla123(self):
        self.cb.addTextMove('e2e5')
        assert self.cb.called_from_pos == (4,6)
        assert self.cb.called_to_pos == (4,3)
