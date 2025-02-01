


module base() {
    cylinder(h=3, r1=7, r2=6, $fn=50);
}


module body() {
    difference(){
        translate([0, 0, 3]){
        scale([1, 1, 1.2])
        sphere(r=6, $fn=50);
        }
        translate([0,0, -5]){
            cube(12, true);
        }
    }
}


module neck() {
    translate([0, 0, 8])
    cylinder(h=4, r1=3, r2=3.5, $fn=50);
}

module head() {
    translate([0, 0, 12]){
    sphere(r=3, $fn=50);
    }
    translate([0, 0, 18])
    scale([1, 1, 1.2])
    sphere(r=4, $fn=50);
}


module king() {
    color("gold"){
        resize([9, 9, 15]){
            base();
            body();
            neck();
            head();
        }
    }
}


module white_pawn() {
    color("#E0E0E0"){
        resize([9, 9, 15]){
            base();
            body();
            neck();
            head();
        }
    }
}



king();
/**
translate([20, 0, 0]) black_pawn();
*/



