module base(){
    cylinder(2,4.5,4.5,$fn=100);
    cylinder(3,4,4,$fn = 100);
    cylinder(10, 3.5,3.5,$fn=100);

    
}

module top(){
    
    hull(){
        translate([0,0,9])cylinder(1,3.5,3.5,$fn = 100);
        translate([0,0,10])cylinder(1, 4,4,$fn=100);
        translate([0,0,11])cylinder(0.5,3.8,3.8,$fn=100);
    }
    translate([0,0,11.5])cylinder(1,4,4,$fn=100);
    difference(){
        translate([0,0,12])cylinder(3,4,4,$fn=100);
        translate([0,0,12])cylinder(3.3,3.3,3.3,$fn=100);
        translate([0,4,14])cube([2,2,5],true);
        translate([0,-4,14])cube([2,2,5],true);
        translate([4,0,14])cube([2,2,5],true);
        translate([-4,0,14])cube([2,2,5],true);
    }
}


module white_rook(){
    color("white"){
        base();
        top();
    }
}

module black_rook(){
    color("#404040"){
        base();
        top();
    }
}


/**
white_rook();
translate([10,0,0])black_rook();

*/
