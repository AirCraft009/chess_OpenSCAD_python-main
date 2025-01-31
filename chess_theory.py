import numpy as np

chess_spaces = np.empty((8,8,2), int)
for x in range(8):
    for y in range(8):
        chess_spaces[x, y] = [x+1, y+1]

print(chess_spaces)


chess_figures = np.array([
    
    ["p", 1],
    ["k", 3],
    ["b", 3],
    ["r", 5],
    ["q", 9],
    ["k",20],
    
])

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
        downshift = pos[1]-1
        downshift_pos = (pos[0]-downshift, pos[1]-downshift) 
        moves = []
        if pos == [1,8] or pos == [8, 1]:
            return moves
        # for x in range (8-downshift_pos[0]-1):
        try:
            for x in range(-1,8):
                moves.append(board[downshift_pos[0]+x, downshift_pos[1]+x])
        except Exception as e:
            return moves

    def get_diagonals_left(self):
        board = chess_spaces
        pos = self.space
        downshift = 8 - pos[1]
        downshift_pos = (pos[0]-downshift, pos[1]+downshift) 
        moves = []
        if pos == [1,1] or pos == [8, 8]:
            return moves
        try:
            for x in range(8):
                if downshift_pos[1] - x-1 < 0:
                    return moves
                moves.append(board[downshift_pos[0]+x-1, downshift_pos[1]-x-1])
        except Exception as e:
            return moves
               
            
    def get_moves(self):
        board = chess_spaces
        position = self.space
        row, col = np.where(board == position)
        row, col = row[0], col[0]
        
        moves = []
        
        # Horizontal and Vertical moves
        for i in range(8):
            if i != col:
                moves.append(board[row + i])  # Same row
            if i != row:
                moves.append(board[col + i*8])  # Same column
        
        # Diagonal moves
        for i in range(1, 8):
            if row - 7*i in board:
                moves.append(board[row-7*i])
            if row - i >= 0 and col - i >= 0:
                moves.append(board[row - i, col - i])
            if row + i < 8 and col - i >= 0:
                moves.append(board[row + i, col - i])
            if row - i >= 0 and col + i < 8:
                moves.append(board[row - i, col + i])
        
        return np.array(moves)

black = team(False)
white = team(True)
q_black = queen([3, 5])
# print(q_black.get_cols())
# print(q_black.get_rows())
print(q_black.get_diagonals_right())
print(q_black.get_diagonals_left())