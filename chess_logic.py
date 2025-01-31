import solid  
import solid.utils
out = "Output.scad"
bauer = solid.import_scad("bauer.scad")
board = solid.import_scad("Schachboard.scad")
knight = solid.import_scad("knight.scad")
rook = solid.import_scad("rook.scad")
white_p = bauer.white_pawn()
board_main = board.checkerboard(7, 7, True)
knight1 = knight.white_knight()
r1 = rook.black_rook()
board1 = solid.translate([-40, -40, -1.5])(board_main)
white_p_sized = solid.color("white")(solid.translate([-5, -5, 1.5])(solid.resize([9, 9, 14])(white_p))) 
knight_white = solid.translate([5,5,0])(knight1)
rook_black = solid.translate([-15,-15,0])(r1)


scene = white_p_sized + board1 + knight_white + rook_black

solid.scad_render_to_file(scene, out)


