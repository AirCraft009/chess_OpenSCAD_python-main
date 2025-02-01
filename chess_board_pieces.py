import numpy as np

board = {x: 0 for x in range(64)}
#it is split up to number of field: piece on field
Pawn = 2
Knight = 4
Bishop = 8
Rook = 16
Queen = 32
King = 64
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
def check_up(space):
        if space <  57:
            space += offset["up"]
            return space
        return -1
        
def check_side_l(space):
    if space != 0 and space % 8 != 0:
        space += offset["left"]
        return space
    return -1
    
def check_side_r(space):
    if space != 7 and (space + 1) % 8 != 0:
        space += offset["right"]         
        return space
    return -1
    
def check_down(space):
    if space > 7:
        space += offset["down"]
        return space
    return -1

def dia_r_up(space):
    if space < 56 and (space + 1) % 8 != 0:
        space += offset["dia_r_up"]
        return space
    return -1

def dia_l_up(space):
    if space < 56 and space % 8 != 0:
        space += offset["dia_l_up"]
        return space
    return -1
def dia_r_down(space):
    if space > 7 and (space +1) % 8 != 0:
        space += offset["dia_r_down"]
        return space
    return -1

def dia_l_down(space):
    if space > 7 and space % 8 != 0:
        space  += offset["dia_l_down"]
        return space
    return -1     
    
white_pieces = {}
black_pieces = {}
for x in range(64):
    can_move[x] = check_up(x), check_down(x), check_side_r(x), check_side_l(x), dia_l_down(x), dia_l_up(x), dia_r_down(x), dia_r_up(x)
    distance_left[x] = x % 8
    distance_right[x] = 7 - (x % 8)
    for i in left_edge:
        if x >= i and x < i + 8:
            distance_bottom[x] = i//8
    distance_top[x] = 7 - distance_bottom[x]
    
            

    



class piece():
    
    def __init__(self, 
                 white: bool,
                 up: bool,
                 down: bool,
                 side : bool,
                 diagonal: bool,
                 points: int,
                 step_size: int,
                 space = None
                 ):
        
        self.white = white
        self.black = -white
        self.up = up
        self.down = down
        self.side = side 
        self.points = points
        self.diagonal = diagonal
        self.space = space
        print(self.space)
        self.movement = self.define_movement()
        self.stepseize = step_size
    
    def define_movement(self):
        move = {}
        for y in can_move:
            square = []  
            square.append(can_move[y][0] if self.up else -1)
            square.append(can_move[y][1] if self.down else -1)
            square.append(can_move[y][2] if self.side else -1)
            square.append(can_move[y][3] if self.side else -1)
            square.append(can_move[y][4] if self.diagonal else -1)
            square.append(can_move[y][5] if self.diagonal else -1)
            square.append(can_move[y][6] if self.diagonal else -1)
            square.append(can_move[y][7] if self.diagonal else -1)
            move[y] = square
        return move
    
    def move(self, target):
        dis_top = distance_top[target]
        dis_left = distance_left[target]
        
        if dis_left == distance_left[self.space] and self.up == True and distance_top[self.space] - dis_top <= self.stepseize:
            self.space = target
            return self.space
        
        if dis_top == distance_top[self.space] and self.side == True and distance_left[self.space] - dis_left <= self.stepseiz:
            self.space = target
            return self.space
        
        
            
            
    

class pawn(piece):
    def __init__(self, white, space=None):
        super().__init__(white, True, False, False, False, 1, 1, space)
    
    def move(self, target):
        dis_top = distance_top[target]
        dis_left = distance_left[target]
        
        if dis_left == distance_left[self.space] and self.up == True and distance_top[self.space] - dis_top <= self.stepseize and self.space < target:
            self.space = target
            return self.space
    
class queen(piece):
    def __init__(self, white,  space=None):
        super().__init__(white, True, True, True, True, 9, 8, space)

class king(piece):
    def __init__(self, white, space=None):
        super().__init__(white, True, True, True, True, 20, 1, space)
        
class rook(piece):
    def __init__(self, white,  space=None):
        super().__init__(white, True, True, True, False, 3, 8, space)
class bishop(piece):
    def __init__(self, white,  space=None):
        super().__init__(white, False, False, False, True, 3, 8, space)
    
                
            
        

        
        
        
        
    
    
pawn1 = pawn(False, 9)
pawn1.move(17)
q1 = queen(True, 9)
q1.move(1)
print (q1.space)