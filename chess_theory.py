import numpy as np

chess_spaces = np.array([
    [f"{chr(97 + col)}{1 + row}", row * 8 + col] 
    for row in range(8) 
    for col in range(8)
])

chess_figures = np.array([
    
    ["p", 1],
    ["k", 3],
    ["b", 3],
    ["r", 5],
    ["q", 9],
    ["k",20],
    
])

class piece():
    def __init__(self):
        self.technical_range = []
        self.practiacal_range = []
        self.can_take = False
        self.space = None
    def move(self, space):
        if space in self.practiacal_range:
            self.space = space
    def move_debug(self, space):
        self.space = space

class team():
    def __init__(self, white: bool):
        self.pieces = chess_figures
        self.spaces = chess_spaces
        if(white):
            self.occupied_spaces = np.array([
                [f"{chr(97 + col)}{1+row}", row * 2 + col]
                for row in range(2)
                for col in range(8)
            ])
        else:
            self.occupied_spaces = np.array([
                [f"{chr(97 + col)}{8-row}", row * 2 + col]
                for row in range(2)
                for col in range(8)
            ])
            
            


black = team(False)
white = team(True)