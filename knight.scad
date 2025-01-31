

module roundedcube(xdim ,ydim ,zdim,rdim){
hull(){
translate([rdim,rdim,0])cylinder(h=zdim,r=rdim);
translate([xdim-rdim,rdim,0])cylinder(h=zdim,r=rdim);

translate([rdim,ydim-rdim,0])cylinder(h=zdim,r=rdim);
translate([xdim-rdim,ydim-rdim,0])cylinder(h=zdim,r=rdim);
}
}


module knight_base() {
    hull(){
        cylinder(h=2, r=4.5, $fn=100);
        translate([0,0,10])cylinder(h=1, r=2, $fn = 100);
        rotate([0,20,0])translate([2,0,5])cube([2, 3, 4],true);
    }
    
}


module knight_head() {
    difference(){
        translate([-2.5,-2.5,11])roundedcube(10,5,5,2,$fn=100);
        translate([2,5,14])rotate([0,0,-10])cube([13,6,7],true);
        translate([2,-5,14])rotate([0,0,10])cube([13,6,7],true);
        translate([7,0,18])rotate([0,15,0])cube([10, 8, 7],true);
    }
}

module white_knight() {
    union() {
        color("white"){
        knight_base();
        knight_head();
        }
    }
}

white_knight();
