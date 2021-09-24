import java.io.*;
import java.util.*;

interface Employee{  
    int cost();  
}  

class Emp1 implements Employee{  
    public int cost()
        {
            return 100;
            
        }  
} 

class Emp2 implements Employee{  
    public int cost()
        {
            return 150;
            
        }  
} 


class GFG
{
	public static void main (String[] args) 
	{
		
		Employee e1 = new Emp1();
		Employee e2 = new Emp2();
		
		int total_cost =120;
		
		int c1 = e1.cost();
		int c2 = e2.cost();
		
		if(total_cost-c1>0)
	        System.out.println("Employee e1 can be hired");
	    else    
	        System.out.println("Employee e1 can not be hired");
	        
	   
	   if(total_cost-c2>0)
	        System.out.println("Employee e2 can be hired");
	    else    
	        System.out.println("Employee e2 can not be hired");
		
		
		
	}
}
