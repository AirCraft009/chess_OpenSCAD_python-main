import solid  
import solid.utils
import Chess

"""
This is the main file of the chess in OpenSCAD project.
It renders a chessboard with pieces in the starting position.
The pieces are rendered from the functions in the other files in this directory.
The positions of the pieces are defined in the chess_logic.py file.

The board is rendered using the checkerboard function from the Schachboard.scad file.
The pieces are rendered using the functions in the other .scad files.
The positions of the pieces are defined in a 2 dimensional array in the chess_logic.py file.
The positions are defined in the algebraic notation (e.g. e4 would be the 4th column and 4th row).

The main function is the fill_board_3d function which is called at the end of this file.
It loops over the positions array and renders the pieces at the corresponding positions.

the read Fen function is used to read a fen string and return the board state as a 2d array
"""

board_theory = Chess.read_Fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

# print(board_theory)
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
board_main = solid.translate([0,0,-3])(board.checkerboard( 7, 7, True))
def fill_board_3d():
    for x in range(64):
        # print(board_theory[x])
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
                white[x] = queen.white_queen()
            elif board_theory[x] == 33:
                black[x] = queen.black_queen()
            elif board_theory[x] == 64:
                white[x] = king.white_king()
            elif board_theory[x] == 65:
                black[x] = king.black_king()
    
    return board_theory


"""def make_scene():
    fill_board_3d()
    main_l = []
    start_L = []
    
    
    for i, x in enumerate(black):
        
        x_tranlated_piece = solid.translate([0, 0, 0])(black[x])
        start_L.append(x_tranlated_piece)
    
    for i in range(2):
        for x in range(8):
            main_l.append(solid.translate([i*10, x*10, 0 ])(start_L[x*(i+1)]))
        
    main_l.reverse()   
    # print(start_L)
    
    scene = board_main + main_l
    return scene"""



def main():
    board_theory = fill_board_3d()
    # print(white)
    start = [0,0,0]
    pieces = []
    shifted_corr = []
    for piece in white:
        pieces.append(solid.translate([5,5,0])(white[piece]))
        
    for piece in black:
        pieces.append(solid.translate([5,5,0])(black[piece]))
    print(board_theory)
    c = 0
    d = 0
    for x in range (8):
        for i in range(8):
            if board_theory[d] != 0:
                shifted_corr.append(solid.translate([10*i, 10*x, 0])(pieces[c]))
                
                c += 1
            d += 1
    # moved = move_up_white(9, 2, shifted_corr)
    # rook_m = move_up_white(0, 5, moved)
    
    scene = board_main  +  shifted_corr
    return scene


def move_up_white(start, num_spaces, rendered_list):
    spaced = 0
    for x in range(start):
        if board_theory[x] != 0:
            spaced += 1
            board_theory[x+8*num_spaces] = board_theory[x]
            board_theory[x] = 0
            
            
    piece = rendered_list[spaced]
    rendered_list.pop(spaced)
    rendered_list.insert(spaced, solid.translate([0, 10*num_spaces, 0])(piece))
    return rendered_list
    
    
            
            


    


solid.scad_render_to_file(main(), out)

