import numpy as np

class Piece():
        def __init__(self, 
                 white: bool,
                 up: bool,
                 down: bool,
                 side : bool,
                 diagonal: bool,
                 points: int,
                 step_size: int,
                 space = None):
        
            self.white = white
            self.black = not white
            self.up = up
            self.down = down
            self.side = side 
            self.points = points
            self.diagonal = diagonal
            self.space = space
            self.stepsize = step_size
            
        def move_up(self, space):
            if self.up and space < 56:
                return space + 8
            return False

        def move_down(self, space):
            if self.down and space > 7:
                return space - 8
            return False

        def move_left(self, space):
            if self.left and space % 8 != 0:
                return space - 1
            return False

        def move_right(self, space):
            if self.right and space % 8 != 7:
                return space + 1
            return False

        def move_up_left(self, space):
            if self.diagonal and space % 8 != 0 and space < 56:
                return space + 7
            return False

        def move_up_right(self, space):
            if self.diagonal and space % 8 != 7 and space < 56:
                return space + 9
            return False

        def move_down_left(self, space):
            if self.diagonal and space % 8 != 0 and space > 7:
                return space - 9
            return False

        def move_down_right(self, space):
            if self.diagonal and space % 8 != 7 and space > 7:
                return space - 7
            return False
        
        
class knight(Piece):
    def __init__(self, 
                 white: bool,
                 points: int,
                 space = None):
        super().__init__(white, False, False, False, False, points, 1, space)
        
        
    
    def move_knight(self):
        knight_moves = [
            (-17, self.space % 8 != 0 and self.space > 16),
            (-15, self.space % 8 != 7 and self.space > 16),
            (-10, self.space % 8 > 1 and self.space > 8),
            (-6, self.space % 8 < 6 and self.space > 8),
            (6, self.space % 8 > 1 and self.space < 56),
            (10, self.space % 8 < 6 and self.space < 56),
            (15, self.space % 8 != 0 and self.space < 48),
            (17, self.space % 8 != 7 and self.space < 48)
        ]
        return [self.space + move for move, condition in knight_moves if condition]