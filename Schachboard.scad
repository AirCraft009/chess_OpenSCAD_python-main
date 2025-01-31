use <bauer.scad>

module checkerboard(x_max, y_max, flip) {
    for (i = [0:1:y_max]) {
        for (x = [0:1:x_max]) {
            translate([10 * x, 10 * i, 0]) {
                if ((x + i) % 2 == 0) {
                    color(flip ? "black" : "white") cube([10,10,3]);
                } else {
                    color(flip ? "white" : "black") cube([10,10,3]);
                }
            }
        }
    }
}

//*
translate([-40, -40, -3])
checkerboard(7, 7, true);
translate([-5, -5,0])
resize([9, 9, 14]){
    color("white")
    white_pawn();
}


