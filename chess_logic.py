import solid  
import solid.utils
out = "Output.scad"
bauer = solid.import_scad("bauer.scad")
board = solid.import_scad("Schachboard.scad")
white_p = bauer.white_pawn()
board_main = board.checkerboard(7, 7, True)
board1 = solid.translate([40, 40, 3])
white_p_sized = solid.resize([9, 9, 14])(white_p)

solid.scad_render_to_file(white_p_sized,  out)
solid.scad_render_to_file(board1, out)

