import solid  
import solid.utils
from chess_board_pieces import pawn
out = "Output.scad"
bauer = solid.import_scad("bauer.scad")
board = solid.import_scad("Schachboard.scad")
knight = solid.import_scad("knight.scad")
rook = solid.import_scad("rook.scad")

board_main = board.checkerboard(7, 7, True)
knight1 = knight.white_knight()
r1 = rook.black_rook()
# board1 = solid.translate([-40, -40, -1.5])(board_main)
def create_move_pawn(mover):
    p1 = pawn(True, 0)
    if p1.white:
        p = bauer.white_pawn()
    else:
        p = bauer.black_pawn()
    p_start = solid.translate([-5, -5, 0])(p)
    if p1.move(mover):
        p_trans = solid.translate([10, 0, 0])(p_start)
        scene = p_trans + board_main
        return p_trans
    
    


"""white_p_sized = solid.color("white")(solid.translate([-5, -5, 1.5])(solid.resize([9, 9, 14])(white_p))) 
knight_white = solid.translate([5,5,0])(knight1)
rook_black = solid.translate([-15,-15,0])(r1)
scene = white_p_sized + board1 + knight_white + rook_black
"""

p1 = pawn(True, 0)
if p1.white:
    p = bauer.white_pawn()
else:
    p = bauer.black_pawn()
p_start = solid.translate([-5, -5, 0])(p)
p1.move(8)
p_trans = solid.translate([10, 0, 0])(p_start)

scene = p_trans + board_main
    




solid.scad_render_to_file(scene, out)


