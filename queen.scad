


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
    translate([0, 0, 8]){
    hull(){
        cylinder(2, 4,4);
        cylinder(2, 3.7, 3.5);
        }
        cylinder(h=25, r1=3, r2=2.8, $fn=50);
    }
}

module head() {
    translate([0, 0, 12]){
        cylinder(3, 4, 4, $fn=50);
    }
    translate([0, 0, 18]){
    cylinder(8, 2, 3, $fn=50);
        translate([0,0,8]){
            cylinder(3,3,3, $fn=100);
            hull(){
                translate([0,0,1])cylinder(1,3,3,$fn=100);
                translate([0,0,3])cylinder(1,1,1);
            }
            translate([0,0,2])cylinder(3,1,1, $fn=100);
        }
    }
}


module white_queen() {
    color("#E0E0E0"){
        resize([9, 9, 20]){
            base();
            body();
            neck();
            translate([0,0,15])head();
        }
    }
}


module black_queen() {
    color("#404040"){
        resize([9, 9, 20]){
            base();
            body();
            neck();
            translate([0,0,15])head();
        }
    }
}



/**
black_king();
translate([20, 0,0]) white_king();

translate([20, 0, 0]) black_pawn();
*/



