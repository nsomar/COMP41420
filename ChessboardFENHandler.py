from copy import deepcopy

class ChessboardFENHandler(object):

    @staticmethod
    def set_fen_code(chessboard, fen):
        """
        Sets the board and states accoring from a Forsyth-Edwards Notation string.
        Ex. 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'
        """
        chessboard._three_rep_stack = []
        chessboard._state_stack = []
        chessboard._moves = []
        chessboard._reason = 0
        chessboard._game_result = 0

        fparts = fen.split()
        newstate = ""

        #BOARD
        for c in fparts[0]:
            if c in "kqrnbpKQRNBP":
                newstate += c
            elif c in "12345678":
                newstate += '.' * int(c)
        #TURN
        newstate += str("wb".index(fparts[1]))

        #CASTLING
        kq = "KQkq"
        for p in kq:
            if p in fparts[2]:
                newstate += "1"
            else:
                newstate += "0"

        #EN PASSANT
        if len(fparts[3]) == 2:
            newstate += str("abcdefgh".index(fparts[3][0].lower()))
            newstate += str("87654321".index(fparts[3][1]))
        else:
            newstate += "00"

        #GAME RESULT
        newstate+="0"

        #HALF COUNT
        newstate+=":%s" % fparts[4]

        chessboard._state_stack.append(newstate)
        chessboard._state_stack_pointer = 1
        chessboard.load_cur_state()

        three_state = [chessboard._white_king_castle,
            chessboard._white_queen_castle,
            chessboard._black_king_castle,
            chessboard._black_queen_castle,
            deepcopy(chessboard._board),
            deepcopy(chessboard._ep)]

        chessboard._three_rep_stack.append(three_state)

        chessboard.update_king_locations()

    @staticmethod
    def generate_fen_code(chessboard):
        """
        Returns the current state as Forsyth-Edwards Notation string.
        """
        s = chessboard._state_stack[chessboard._state_stack_pointer-1]

        b= s[:64]
        v = s[64:72]
        fifty =  s[73:]

        rows = []
        for i in range(8):
            row = b[i*8:(i+1)*8]
            cnt = 0; res = ""
            for c in row:
                if c == ".":
                    cnt+=1
                else:
                    if cnt:
                        res += str(cnt);
                        cnt=0
                    res+=c
            if cnt:
                res += str(cnt)
            rows.append(res)
        board = "/".join(rows)

        turn = (["w", "b"])[int(v[0])]

        kq = ""
        if int(v[1]): kq+="K"
        if int(v[2]): kq+="Q"
        if int(v[3]): kq+="k"
        if int(v[4]): kq+="q"
        if not kq:
            kq = "-"

        x = int(v[5])
        y = int(v[6])
        ep = "-"
        if not (x == 0 and y == 0):
            if turn == "b" and (chessboard._board[y][x-1] == 'p' or chessboard._board[y][x+1] == 'p'):
                ep = "%s%s" % ( ("abcdefgh")[x], ("87654321")[y+1])
            elif turn == "w" and (chessboard._board[y][x-1] == 'P' or chessboard._board[y][x+1] == 'P'):
                ep = "%s%s" % ( ("abcdefgh")[x], ("87654321")[y-1])

        move = (chessboard._state_stack_pointer+1)/2

        return "%s %s %s %s %s %d" % (board, turn, kq, ep, fifty, move)
