import numpy as np
from Piece import Piece, knight
import random

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
                white_pieces[x] = Piece(True, True, False, False, False, 1, 1, 2, x)
            elif board[x] == 3:
                black_pieces[x] = Piece(False, True, False, False, False, 1, 1, 3, x)
            elif board[x] == 4:
                white_pieces[x] = knight(True, 3, 4, x)
                #knight
                # white_pieces[x] = Piece(True, False, False, False, False, 1, 1, x)
            elif board[x] == 5:
                black_pieces[x] = knight(False, 3, 5, x)
                #knight
                # white_pieces[x] = Piece(True, True, False, False, False, 1, 1, x)
            elif board[x] == 8:
                white_pieces[x] = Piece(True, False, False, False, True, 3, 8, 8,x)
            elif board[x] == 9:
                black_pieces[x] = Piece(False, False, False, False, True, 3, 8, 9, x)
            elif board[x] == 16:
                white_pieces[x] = Piece(True, True, True, True, False, 5, 8, 16, x)
            elif board[x] == 17:
                black_pieces[x] = Piece(False, True, True, True, False, 5, 8, 17, x)
            elif board[x] == 32:
                white_pieces[x] = Piece(True, True, True, True, True, 9, 8, 32, x)
            elif board[x] == 33:
                black_pieces[x] = Piece(False, True, True, True, True, 9, 8, 33, x)
            elif board[x] == 64:
                white_pieces[x] = Piece(True, True, False, False, False, 20, 1, 64, x)
            elif board[x] == 65:
                black_pieces[x] = Piece(False, True, False, False, False, 1, 1, 65, x)

def visualise_fen():
    pass          
            
class ChessBot():
    
    def __init__(self, color: bool, pieces: dict):
        self.white = color
        self.blaxk = not color
        self.pieces = pieces
        self.turn = color
        self.possible_moves = {}
        self.capture_material = 0 
        self.material = 0
        
        
    def calc_material(self):
        for mat in self.pieces:
            self.material += self.pieces[mat].points*100
        return self.material
            
    def move_random(self):
        itemlist = []
        if len(self.possible_moves) == 0:
            self.Generate_move(1)
        
        for item in self.possible_moves.items():
            itemlist.append(item)
            
        rand_piece_key, possible_spaces = random.choice(itemlist)
        selected_space = random.choice(possible_spaces)
        
        # Remove the piece from its current location on the board
        board.pop(selected_space)
        pos = rand_piece_key.space
        self.pieces.pop(pos)
        
        
        # Update the piece's space
        
        self.pieces[selected_space] = rand_piece_key
        
        # Place the piece at its new location on the board
        board[selected_space] = self.pieces[selected_space].index
        
        # Update white pieces if the piece is white
        if self.white:
            white_pieces = self.pieces
        else:
            black_pieces = self.pieces
                            
    def Generate_move(self, depth):
        if depth == 0:
            return 1
        depth -= 1
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
                        # if piece.stepsize == 1:
                            # print("Pawn")
                        if board[target] == 0:
                            moves.append(target) 
                            
                        elif board[target] % 2 == piece_num % 2:
                            break
                        
                        else:
                            moves.append(target)
                            self.capture_material += board[target] * 100
                        self.possible_moves[piece] = moves
                    elif type(piece) == knight:
                        # print("knight")
                        n_moves = piece.move_knight()
                        for i, move in enumerate(n_moves):
                            if board[move] == 0:
                                self.possible_moves[piece] = n_moves
                                 
                                
                            elif board[move] % 2 == piece_num % 2:
                                n_moves.pop(i)
                            
                            else:
                                self.possible_moves[piece] = n_moves
                                self.capture_material += board[move] * 100
                                break
                        
                            
        # self.move_random()                                
        self.Generate_move(depth)
        return self.possible_moves
                                
                            
            
                    
        
        


        
        
if __name__ == "__main__":
    print(read_Fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"))
    def get_board():
        return board
    fill_board()
    white_bot = ChessBot(True, white_pieces)
    # print(white_bot.Generate_move(2))
    # print(white_bot.capture_material)
    # print(white_bot.calc_material())
    white_bot.Generate_move(1)
    # print(board)
    white_bot.move_random()
    print("-------------------")
    print(board)
        