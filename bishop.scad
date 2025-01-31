module body(){
    cylinder(2,4.5,4.5,$fn=100);
    hull(){
        translate([0,0,1])cylinder(1,4.2,4.2,$fn=100);
        translate([0,0,2])cylinder(1,4.8,4.8,$fn=100);
        translate([0,0,3])cylinder(1,4.2,4.2,$fn=100);
    }
    hull(){
        
        translate([0,0,4])cylinder(1,3.6,3.6,$fn=100);
        translate([0,0,12])cylinder(1,2,2,$fn=100);
    }
    hull(){
        translate([0,0,12])cylinder(1,2,2,$fn=100);
        translate([0,0,13])cylinder(1,3,3,$fn=100);
    
    }
    difference(){
        hull(){
            translate([0,0,16])sphere(3,$fn=100);
            translate([0,0,19])sphere(2,$fn=100);
        }
        translate([1,1,18])rotate([0,60,0])cube([1,8,5],$fn=100,true);
    }
}


module white_bishop(){
    color("white")
    body(); 
}

module black_bishop(){
    color("#404040")
    body();
}
/**
black_bishop();
translate([10,0,0])white_bishop();
*/