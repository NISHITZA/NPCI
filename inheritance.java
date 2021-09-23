import java.io.*;
import java.util.*;

class Vehicle{
    
    static void info()
    {
        System.out.println("Display info");
    }
}

class CarA extends Vehicle{
    
    int wheel(){
        
        return 4;
    }
}

class BikeA extends Vehicle{
    
    int wheel(){
        
        return 2;
    }
}




class GFG extends CarA, BikeA
{
	public static void main (String[] args) 
	{
		
		
		CarA a = new CarA();
		BikeA b = new BikeA();
	    int spare =0;
	    spare = a.wheel()+b.wheel() ;
	
	    System.out.println("The spare "+spare);
		
		
		
	}
}
