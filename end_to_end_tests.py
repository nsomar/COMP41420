import unittest
from ChessBoard import ChessBoard


class EndToEndTests(unittest.TestCase):

    def setUp(self):
        self.cb = ChessBoard()

    def test_moving_to_e2e4(self):
        self.cb.add_text_move('e2e4')
        assert self.cb.state2str() == "rnbqkbnrpppppppp....................P...........PPPP.PPPRNBQKBNR11111440:0"

    def test_moving_to_e2e4_f7f5(self):
        self.cb.add_text_move('e2e4')
        self.cb.add_text_move('f7f5')
        assert self.cb.state2str() == "rnbqkbnrppppp.pp.............p......P...........PPPP.PPPRNBQKBNR01111530:0"

    def test_moving_to_e2e4_f7f5_e4f5(self):
        self.cb.add_text_move('e2e4')
        self.cb.add_text_move('f7f5')
        self.cb.add_text_move('e4f5')
        assert self.cb.state2str() == "rnbqkbnrppppp.pp.............P..................PPPP.PPPRNBQKBNR11111000:0"

    def test_moving_to_e2e4_f7f5_e4f5_g8h6(self):
        self.cb.add_text_move('e2e4')
        self.cb.add_text_move('f7f5')
        self.cb.add_text_move('e4f5')
        self.cb.add_text_move('g8h6')
        assert self.cb.state2str() == "rnbqkb.rppppp.pp.......n.....P..................PPPP.PPPRNBQKBNR01111000:1"

    def test_moving_to_e2e4_f7f5_e4f5_g8h6_f1d3(self):
        self.cb.add_text_move('e2e4')
        self.cb.add_text_move('f7f5')
        self.cb.add_text_move('e4f5')
        self.cb.add_text_move('g8h6')
        self.cb.add_text_move('f1d3')
        assert self.cb.state2str() == "rnbqkb.rppppp.pp.......n.....P.............B....PPPP.PPPRNBQK.NR11111000:2"