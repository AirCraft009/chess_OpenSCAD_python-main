// Generated by SolidPython 1.1.3 on 2025-02-02 12:19:57
use <C:/Users/cocon/Documents/programming/3d modelling/chess_OpenSCAD_python-main/Schachboard.scad>
use <C:/Users/cocon/Documents/programming/3d modelling/chess_OpenSCAD_python-main/bauer.scad>
use <C:/Users/cocon/Documents/programming/3d modelling/chess_OpenSCAD_python-main/knight.scad>
use <C:/Users/cocon/Documents/programming/3d modelling/chess_OpenSCAD_python-main/rook.scad>
use <C:/Users/cocon/Documents/programming/3d modelling/chess_OpenSCAD_python-main/king.scad>
use <C:/Users/cocon/Documents/programming/3d modelling/chess_OpenSCAD_python-main/queen.scad>
use <C:/Users/cocon/Documents/programming/3d modelling/chess_OpenSCAD_python-main/bishop.scad>


union() {
	translate(v = [0, 0, -3]) {
		checkerboard(flip = true, x_max = 7, y_max = 7);
	}
	translate(v = [0, 0, 0]) {
		translate(v = [5, 5, 0]) {
			white_rook();
		}
	}
	translate(v = [10, 0, 0]) {
		translate(v = [5, 5, 0]) {
			white_knight();
		}
	}
	translate(v = [20, 0, 0]) {
		translate(v = [5, 5, 0]) {
			white_bishop();
		}
	}
	translate(v = [30, 0, 0]) {
		translate(v = [5, 5, 0]) {
			king();
		}
	}
	translate(v = [40, 0, 0]) {
		translate(v = [5, 5, 0]) {
			queen();
		}
	}
	translate(v = [50, 0, 0]) {
		translate(v = [5, 5, 0]) {
			white_bishop();
		}
	}
	translate(v = [60, 0, 0]) {
		translate(v = [5, 5, 0]) {
			white_knight();
		}
	}
	translate(v = [70, 0, 0]) {
		translate(v = [5, 5, 0]) {
			white_rook();
		}
	}
	translate(v = [0, 10, 0]) {
		translate(v = [5, 5, 0]) {
			white_pawn();
		}
	}
	translate(v = [10, 10, 0]) {
		translate(v = [5, 5, 0]) {
			white_pawn();
		}
	}
	translate(v = [20, 10, 0]) {
		translate(v = [5, 5, 0]) {
			white_pawn();
		}
	}
	translate(v = [30, 10, 0]) {
		translate(v = [5, 5, 0]) {
			white_pawn();
		}
	}
	translate(v = [40, 10, 0]) {
		translate(v = [5, 5, 0]) {
			white_pawn();
		}
	}
	translate(v = [50, 10, 0]) {
		translate(v = [5, 5, 0]) {
			white_pawn();
		}
	}
	translate(v = [60, 10, 0]) {
		translate(v = [5, 5, 0]) {
			white_pawn();
		}
	}
	translate(v = [70, 10, 0]) {
		translate(v = [5, 5, 0]) {
			white_pawn();
		}
	}
	translate(v = [0, 60, 0]) {
		translate(v = [5, 5, 0]) {
			black_pawn();
		}
	}
	translate(v = [10, 60, 0]) {
		translate(v = [5, 5, 0]) {
			black_pawn();
		}
	}
	translate(v = [20, 60, 0]) {
		translate(v = [5, 5, 0]) {
			black_pawn();
		}
	}
	translate(v = [30, 60, 0]) {
		translate(v = [5, 5, 0]) {
			black_pawn();
		}
	}
	translate(v = [40, 60, 0]) {
		translate(v = [5, 5, 0]) {
			black_pawn();
		}
	}
	translate(v = [50, 60, 0]) {
		translate(v = [5, 5, 0]) {
			black_pawn();
		}
	}
	translate(v = [60, 60, 0]) {
		translate(v = [5, 5, 0]) {
			black_pawn();
		}
	}
	translate(v = [70, 60, 0]) {
		translate(v = [5, 5, 0]) {
			black_pawn();
		}
	}
	translate(v = [0, 70, 0]) {
		translate(v = [5, 5, 0]) {
			black_rook();
		}
	}
	translate(v = [10, 70, 0]) {
		translate(v = [5, 5, 0]) {
			color(alpha = 1.0000000000, c = "black") {
				white_knight();
			}
		}
	}
	translate(v = [20, 70, 0]) {
		translate(v = [5, 5, 0]) {
			black_bishop();
		}
	}
	translate(v = [30, 70, 0]) {
		translate(v = [5, 5, 0]) {
			king();
		}
	}
	translate(v = [40, 70, 0]) {
		translate(v = [5, 5, 0]) {
			queen();
		}
	}
	translate(v = [50, 70, 0]) {
		translate(v = [5, 5, 0]) {
			black_bishop();
		}
	}
	translate(v = [60, 70, 0]) {
		translate(v = [5, 5, 0]) {
			color(alpha = 1.0000000000, c = "black") {
				white_knight();
			}
		}
	}
	translate(v = [70, 70, 0]) {
		translate(v = [5, 5, 0]) {
			black_rook();
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
import solid  
import solid.utils
import Chess

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
                white[x] = queen.queen()
            elif board_theory[x] == 33:
                black[x] = queen.queen()
            elif board_theory[x] == 64:
                white[x] = king.king()
            elif board_theory[x] == 65:
                black[x] = king.king()
    
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



def test():
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
    
    scene = board_main  + shifted_corr
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
    
    
            
            


    


solid.scad_render_to_file(test(), out)

 
 
************************************************/
