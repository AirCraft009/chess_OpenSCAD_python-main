import numpy as np
import itertools

chess_spaces = np.empty((8,8,2), int)
for x in range(8):
    for y in range(8):
        chess_spaces[x, y] = [x+1, y+1]

# print(chess_spaces)


chess_figures = np.array([
    
    ["p", 1],
    ["k", 3],
    ["b", 3],
    ["r", 5],
    ["q", 9],
    ["k",20],
    
])

def remove_duplicates(lst):
    seen = {}
    return [seen.setdefault(x, x) for x in lst if x not in seen]

class piece():
    def __init__(self, space, points, piece_name):
        self.technical_range = []
        self.practiacal_range = []
        self.can_take = False
        self.space = space
        self.points = points
        self.name = piece_name
        
        
    def move(self, space):
        if space in self.practiacal_range:
            self.space = space
    def move_debug(self, space):
        self.space = space

class team():
    def __init__(self, white: bool):
        self.pieces = chess_figures
        self.spaces = chess_spaces
        self.occupied_spaces = np.array([])
        if(white):
            for x in range(2):
                for y in range(8):
                    self.occupied_spaces = np.append(self.occupied_spaces, y)
        else:
            for x in range(48, 65):
                for y in range(8):
                    self.occupied_spaces = np.append(self.occupied_spaces, y)
            

class queen(piece):
    def __init__(self, space,):
        super().__init__(space, 9, "q")
        self.get_moves()
        # self.technical_range  = self.get_moves()
        # print(self.technical_range)
    
    def get_rows(self):
        board = chess_spaces
        position = self.space
        moves = []
        for x in range(1, 8- position[0]+1):
            moves.append(board[position[0]+3-x,position[1]-1])
        for x in range(1, position[0]+1):
            moves.append(board[position[0]-x,position[1]-1])
        return moves    
    
    def get_cols(self):
        
        board = chess_spaces
        position = self.space
        return [board[position[0]-1]]
    
    def get_diagonals_right(self):
        board = chess_spaces
        pos = self.space
        downshift = pos[1] - 1
        downshift_pos = (pos[0] - downshift, pos[1] - downshift) 
        moves = []

        if np.array_equal(pos, [1, 8]) or np.array_equal(pos, [8, 1]):
            return moves

        for x in range(-1, 8):
            new_x = downshift_pos[0] + x
            new_y = downshift_pos[1] + x
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                moves.append(board[new_x, new_y])
        return moves

    def get_diagonals_left(self):
        board = chess_spaces
        pos = self.space
        downshift = 8 - pos[1]
        downshift_pos = (pos[0] - downshift, pos[1] + downshift) 
        moves = []

        if np.array_equal(pos, [1, 1]) or np.array_equal(pos, [8, 8]):
            return moves

        for x in range(8):
            new_x = downshift_pos[0] + x
            new_y = downshift_pos[1] - x
            if new_y < 0:
                break
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                moves.append(board[new_x, new_y])
        return moves
               
            
    def get_moves(self):
        for item in self.get_rows():
            for under in item:
                self.technical_range.append(under)
                
        for item in self.get_cols():
            for under in item:
                    for idk in under:
                        self.technical_range.append(idk)
            
        for item in self.get_diagonals_right():
            for under in item:
                self.technical_range.append(under)
                
        for item in self.get_diagonals_left():
            for under in item:
                self.technical_range.append(under)
        # self.technical_range = remove_duplicates(self.technical_range)

        x = []
        techR = self.technical_range
        for col_Row in zip(techR, techR[1:]):
            x.append(col_Row)
        self.technical_range.clear()
        self.technical_range = x
        # print(self.technical_range)
        return self.technical_range
    
    
class king(piece):
    def __init__(self, space):
        super().__init__(space, 20, "k")
        self.get_moves()
    
    def get_rows(self, pos):
        board = chess_spaces
        position = pos
        moves = []
        for x in range(1, 8- position[0]+1):
            moves.append(board[position[0]+3-x,position[1]-1])
        for x in range(1, position[0]+1):
            moves.append(board[position[0]-x,position[1]-1])
        return moves
    
    def get_cols(self, pos):
        
        board = chess_spaces
        position = pos
        return [board[position[0]-1]]   
    def get_moves(self):
        pos = self.space
        board = chess_spaces

        # Check valid moves by ensuring the indices are within the board range (0-7)
        valid_moves = [
            (pos[0] - 1, pos[1]),        # move 1
            (pos[0], pos[1]),            # move 2
            (pos[0], pos[1] - 1),        # move 3
            (pos[0] - 2, pos[1] - 1),    # move 4
            (pos[0] - 2, pos[1] - 2),    # move 5
            (pos[0] - 2, pos[1]),        # move 6
            (pos[0], pos[1] - 2),        # move 7
            (pos[0] - 1, pos[1] - 2)     # move 8
        ]

        # Filter out moves that are outside the board boundaries
        for move in valid_moves:
            x, y = move
            if 0 <= x < 8 and 0 <= y < 8:  # Ensure the move is within board limits
                self.technical_range.append(board[x, y])
        print(self.technical_range)
        return self.technical_range
    
class rook(piece):
    def __init__(self, space):
        super().__init__(space, 5, "r")
        self.get_moves()
        
    def get_cols(self):
        board = chess_spaces
        position = self.space
        return [board[position[0]-1]]
        
    def get_rows(self):
        board = chess_spaces
        position = self.space
        moves = []
        for x in range(1, 8- position[0]+1):
            moves.append(board[position[0]+3-x,position[1]-1])
        for x in range(1, position[0]+1):
            moves.append(board[position[0]-x,position[1]-1])
        return moves
    
    
    def get_moves(self):
        pos = self.space
        board = chess_spaces
        self.technical_range.clear()
        for row in self.get_rows():
            for item in row:
                # print(item)
                self.technical_range.append(item)
                    
        for col in self.get_cols():
            for item in col:
                for under in item:
                    # print(under)
                    self.technical_range.append(under)
        #es scheint mir so als hätte die original liste sich mit dder techR liste im buffer verbunden deshalb werden beim clearen der ersten auch die ELemente der zweite neutralisiert.
        x = []
        techR = self.technical_range
        for col_Row in zip(techR, techR[1:]):
            x.append(col_Row)
        self.technical_range.clear()
        self.technical_range = x
        # print(self.technical_range)
        return self.technical_range
    
    
    
class bishop(piece):
        def __init__(self, space):
            super().__init__(space, 3, "b")
            self.get_moves()
        
        def diagonals_right(self):
            board = chess_spaces
            pos = self.space
            downshift = pos[1] - 1
            downshift_pos = (pos[0] - downshift, pos[1] - downshift) 
            moves = []

            if np.array_equal(pos, [1, 8]) or np.array_equal(pos, [8, 1]):
                return moves
            for x in range(-1, 8):
                new_x = downshift_pos[0] + x
                new_y = downshift_pos[1] + x
                if new_x < 0 or new_x > 7 or new_y < 0 or new_y > 7:
                    break
                moves.append(board[new_x, new_y])
            return moves
        
        def diagonals_left(self):
            board = chess_spaces
            pos = self.space
            downshift = pos[1] - 1
            downshift_pos = (pos[0] - downshift, pos[1] - downshift) 
            moves = []

            if np.array_equal(pos, [1, 1]) or np.array_equal(pos, [8, 8]):
                return moves

            for x in range(-1, 8):
                new_x = downshift_pos[0] - x
                new_y = downshift_pos[1] - x
                if new_x < 0 or new_x > 7 or new_y <    0 or new_y > 7:
                    break
                moves.append(board[new_x, new_y])
            return moves
        
        def get_moves(self):
            pos = self.space
            board = chess_spaces
            self.technical_range.clear()
            for row in self.diagonals_right():
                for item in row:
                    # print(item)
                    self.technical_range.append(item)
                    
            for col in self.diagonals_left():
                for item in col:
                        # print(under)
                        self.technical_range.append(item)
            
            x = []
            techR = self.technical_range
            for col_Row in zip(techR, techR[1:]):
                x.append(col_Row)
            self.technical_range.clear()
            self.technical_range = x
            print(self.technical_range)    
            return self.technical_range
        

    



black = team(False)
white = team(True)
q_black = queen([1, 5])
# print(q_black.get_cols())
# print(q_black.get_rows())
# print(q_black.get_diagonals_right())
# print(q_black.get_diagonals_left())
# print(q_black.get_moves())
# king1 = king([4,5])
# king1.get_moves()
rook1 = rook([1,1])
# print(rook1.get_cols())
# print(rook1.get_rows())
# rook1.get_moves()
bis1 = bishop([4,5])
# bis1.get_moves()
print(bis1.diagonals_right())
print(bis1.diagonals_left())