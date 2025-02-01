import solid  
import solid.utils
import Chess

board_theory = Chess.read_Fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
Chess.fill_board()
white, black = Chess.white_pieces, Chess.black_pieces
out = "Output.scad"
bauer = solid.import_scad("bauer.scad")
board = solid.import_scad("Schachboard.scad")
knight = solid.import_scad("knight.scad")
rook = solid.import_scad("rook.scad")
start_space = [75, 5, 0]

board_main = solid.translate([0,0, -3])(board.checkerboard(7, 7, True))
p = solid.translate(start_space)(bauer.white_pawn())
scene = board_main + p
def start_up():    
    pass

def make_start_space():
    piece_num = []
    for piece in range(8):
        if white[piece].space != None:
            print(white[piece].space)
            piece_space = solid.translate([start_space[0], start_space[1]+piece*10, start_space[2] ])(bauer.white_pawn())
            piece_num.append(piece_space)
            scene = board_main + piece_num
    return scene
    


solid.scad_render_to_file(make_start_space(), out)


