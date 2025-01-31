import solid  
import solid.utils

bauer = solid.import_scad("bauer.scad")
board = solid.import_scad("Schachboard.scad")
white_p = bauer.white_pawn()
white_p_sized = solid.resize([9, 9, 14])(white_p)

solid.scad_render_to_file(white_p_sized, "Output.scad")

