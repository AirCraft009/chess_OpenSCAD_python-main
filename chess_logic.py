import solid  
import solid.utils
import Chess

board_theory = Chess.read_Fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
print(board_theory)
Chess.fill_board()
white, black = Chess.white_pieces, Chess.black_pieces
out = "Output.scad"
bauer = solid.import_scad("bauer.scad")
board = solid.import_scad("Schachboard.scad")
knight = solid.import_scad("knight.scad")
rook = solid.import_scad("rook.scad")
king = solid.import_scad("king.scad")
queen = solid.import_scad("queen.scad")
bishop = solid.import_scad("bishop.scad")
white_pawn = bauer.white_pawn()
board_main = board.checkerboard( 7, 7, True)
def fill_board_3d():
    for x in range(64):
        if board_theory[x] != 0:
            if board_theory[x] == 2:
                white[x] = bauer.white_pawn()
            elif board_theory[x] == 3:
                black[x] = bauer.black_pawn()
            elif board_theory[x] == 4:
                white[x] = knight.white_knight()
            elif board_theory[x] == 5:
                black[x] = solid.color("black")(knight.white_knight())
            elif board_theory[x] == 8:
                white[x] = bishop.white_bishop()
            elif board_theory[x] == 9:
                black[x] = bishop.black_bishop()
            elif board_theory[x] == 16:
                white[x] = rook.white_rook()
            elif board_theory[x] == 17:
                black[x] = rook.black_rook()
            elif board_theory[x] == 32:
                white[x] = queen.queen()
            elif board_theory[x] == 33:
                black[x] = queen.queen()
            elif board_theory[x] == 64:
                white[x] = king.king()
            elif board_theory[x] == 65:
                black[x] = king.king()
    return white, black

def make_scene():
    fill_board_3d()
    main_l = []
    for x in black:
        x_tranlated_piece = solid.translate([75, 5*x*10, 0])(black[x])
        main_l.append(x_tranlated_piece)
        
        
    
    scene = [board_main + x 
    return 


    


solid.scad_render_to_file(make_scene(), out)


