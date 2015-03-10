import unittest
from ChessBoard import ChessBoard


class FENTests(unittest.TestCase):

    """
        FEN correct strings are provided from http://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
    """

    """
        Test getting fen notion
    """
    def setUp(self):
        self.cb = ChessBoard()

    def test_that_it_generates_correct_fen_starting_position(self):
        assert self.cb.get_fen_code() == "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    def test_that_it_generates_correct_for_e2e3(self):
        self.cb.add_text_move('e2e3')
        assert self.cb.get_fen_code() == "rnbqkbnr/pppppppp/8/8/8/4P3/PPPP1PPP/RNBQKBNR b KQkq - 0 1"

    def test_that_it_generates_correct_for_a7a5(self):
        self.cb.add_text_move('e2e3')
        self.cb.add_text_move('a7a5')
        assert self.cb.get_fen_code() == "rnbqkbnr/1ppppppp/8/p7/8/4P3/PPPP1PPP/RNBQKBNR w KQkq - 0 2"

    def test_that_it_generates_correct_for_e3e4(self):
        self.cb.add_text_move('e2e3')
        self.cb.add_text_move('a7a5')
        self.cb.add_text_move('e3e4')
        assert self.cb.get_fen_code() == "rnbqkbnr/1ppppppp/8/p7/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2"

    def test_that_it_generates_correct_fen_for_pawn_eating_pawn(self):
        self.cb.add_text_move('e2e4')
        self.cb.add_text_move('f7f5')
        self.cb.add_text_move('e4f5')

        assert self.cb.get_fen_code() == "rnbqkbnr/ppppp1pp/8/5P2/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2"

    """
        Test moving by settings fen
    """
    def test_that_it_set_fen_for_e2e3(self):
        assert self.cb._board[6][4] == "P"
        self.cb.set_fen_code("rnbqkbnr/pppppppp/8/8/8/4P3/PPPP1PPP/RNBQKBNR b KQkq - 0 1")
        assert self.cb._board[6][4] == "."

    def test_that_it_set_fen_for_a7a5(self):
        assert self.cb._board[6][4] == "P"
        assert self.cb._board[1][0] == "p"
        self.cb.set_fen_code("rnbqkbnr/1ppppppp/8/p7/8/4P3/PPPP1PPP/RNBQKBNR w KQkq - 0 2")
        # after moving
        assert self.cb._board[1][0] == "."
        assert self.cb._board[6][4] == "."

    def test_that_it_set_fen_for_e3e4(self):
        assert self.cb._board[6][4] == "P"
        print self.cb._board[4][5] == "."
        self.cb.set_fen_code("rnbqkbnr/1ppppppp/8/p7/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2")
        # after moving
        print self.cb._board[4][5] == "P"
        assert self.cb._board[1][0] == "."

    def test_that_it_sets_correct_fen_for_pawn_eating_pawn(self):
        assert self.cb._board[3][5] == "."
        assert pieces_count(self.cb._board) == 32
        self.cb.set_fen_code("rnbqkbnr/ppppp1pp/8/5P2/8/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2")
        assert self.cb._board[3][5] == "P"
        assert pieces_count(self.cb._board) == 31


def pieces_count(board):
    count = 0
    for row in board:
        for item in row:
            if item != ".":
                count += 1

    return count
