import numpy as np
from Piece import Piece, knight

board = {x: 0 for x in range(64)}
#it is split up to number of field: piece on field
Pawn = 2
Pawnb = 3
Knight = 4
Knightb = 5
Bishop = 8
Bishopb = 9
Rook = 16
Rookb = 17
Queen = 32
Queenb = 33
King = 64
Kingb = 65
can_move = {}
offset = {
    "up": 8,
    "down": -8,
    "left": -1,
    "right": 1,
    "dia_r_up": 9,
    "dia_r_down": -7,
    "dia_l_down": -9,
    "dia_l_up": 7
}

left_edge = [0, 8, 16, 24, 32, 40, 48, 56]
bootom = [0, 1, 2, 3, 4, 5, 6, 7]
distance_top = {}
distance_left = {}
distance_right = {}
distance_bottom = {}


white_pieces = {}
black_pieces = {}
for x in range(64):
    distance_left[x] = x % 8
    distance_right[x] = 7 - (x % 8)
    for i in left_edge:
        if x >= i and x < i + 8:
            distance_bottom[x] = i//8
    distance_top[x] = 7 - distance_bottom[x]
    
def read_Fen(note):
    start = 64
    flip = True
    for piece in note.split("/"):
        note = note[::-1]
        for i, x in enumerate(list(piece)):
            try:
                y = int(x)
                start -= y
            except ValueError:
                start -= 1
                if x == "P":
                    board[start] = Pawn
                elif x == "B":
                    board[start] = Bishop
                elif x == "R":
                    board[start] = Rook
                elif x == "Q":
                    board[start] = Queen
                elif x == "K":
                    board[start] = King
                elif x == "N":
                    board[start] = Knight
                elif x == "p":
                    board[start] = Pawnb
                elif x == "b":
                    board[start] = Bishopb
                elif x == "r":
                    board[start] = Rookb
                elif x == "q":
                    board[start] = Queenb
                elif x == "k":
                    board[start] = Kingb
                elif x == "n":
                    board[start] = Knightb
                elif x == "/":
                    flip = not flip
                else:
                    pass
            
    return board

def fill_board():
    for x in range(64):
        if board[x] != 0:
            if board[x] == 2:
                white_pieces[x] = Piece(True, True, False, False, False, 1, 1, x)
            elif board[x] == 3:
                black_pieces[x] = Piece(False, True, False, False, False, 1, 1, x)
            elif board[x] == 4:
                white_pieces[x] = knight(True, 3, x)
                #knight
                # white_pieces[x] = Piece(True, False, False, False, False, 1, 1, x)
            elif board[x] == 5:
                black_pieces[x] = knight(False, 3, x)
                #knight
                # white_pieces[x] = Piece(True, True, False, False, False, 1, 1, x)
            elif board[x] == 8:
                white_pieces[x] = Piece(True, False, False, False, True, 3, 8, x)
            elif board[x] == 9:
                black_pieces[x] = Piece(False, False, False, False, True, 3, 8, x)
            elif board[x] == 16:
                white_pieces[x] = Piece(True, True, True, True, False, 5, 8, x)
            elif board[x] == 17:
                black_pieces[x] = Piece(False, True, True, True, False, 5, 8, x)
            elif board[x] == 32:
                white_pieces[x] = Piece(True, True, True, True, True, 9, 8, x)
            elif board[x] == 33:
                black_pieces[x] = Piece(False, True, True, True, True, 9, 8, x)
            elif board[x] == 64:
                white_pieces[x] = Piece(True, True, False, False, False, 20, 1, x)
            elif board[x] == 65:
                black_pieces[x] = Piece(False, True, False, False, False, 1, 1, x)
            
            
class ChessBot():
    
    def __init__(self, color: bool, pieces: dict):
        self.white = color
        self.blaxk = not color
        self.pieces = pieces
        self.turn = color
        self.possible_moves = {}
        self.capture_material = 0 
        self.material = 0
        
    def Generate_move(self):
        
        moves = []
        for x in self.pieces:
            moves = []
            piece_num = board[x]
            piece = self.pieces[x]
            if piece.white == self.white:
                target = piece.space
                for i in range(piece.stepsize):
                    target = piece.move_up(target )
                    if type(target) == int:
                        if piece.stepsize == 1:
                            print("Pawn")
                        if board[target] == 0:
                            moves.append(target) 
                            
                        elif board[target] % 2 == piece_num % 2:
                            break
                        
                        else:
                            self.possible_moves[piece] = target
                            self.capture_material += board[target] * 100
                    elif type(piece) == knight:
                        print("knight")
                        n_moves = piece.move_knight()
                        for move in n_moves:
                            if board[move] == 0:
                                self.possible_moves[piece] = n_moves
                                break 
                                
                            elif board[move] % 2 == piece_num % 2:
                                continue
                            
                            else:
                                self.possible_moves[move] = n_moves
                                self.capture_material += board[move] * 100
                                break
                                
            self.possible_moves[piece] = moves
                                
                        
        return self.possible_moves
                                
                            
        """if piece.move_down():
                        self.possible_moves.append()
                    if piece.move_left():
                        self.possible_moves.append()
                    if piece.move_right():
                        self.possible_moves.append()
                    if piece.move_up_left():
                        self.possible_moves.append()
                    if piece.move_up_right():
                        self.possible_moves.append()
                    if piece.move_down_left():
                        self.possible_moves.append()
                    if piece.move_down_right():
                        self.possible_moves.append()
                """    
                    
        
        


        
        
if __name__ == "__main__":
    print(read_Fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"))
    def get_board():
        return board
    fill_board()
    white_bot = ChessBot(True, white_pieces)
    print(white_bot.Generate_move())
    print(white_bot.capture_material)
        