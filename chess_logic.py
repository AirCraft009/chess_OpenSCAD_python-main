import solid  
import solid.utils
out = "Output.scad"
bauer = solid.import_scad("bauer.scad")
board = solid.import_scad("Schachboard.scad")
white_p = bauer.white_pawn()
board_main = board.checkerboard(7, 7, True)
board1 = solid.translate([-40, -40, -1.5])(board_main)
white_p_sized = solid.translate([-5, -5, 1.5])(solid.resize([9, 9, 14])(white_p)) 

scene = white_p_sized + board1

solid.scad_render_to_file(scene, out)


