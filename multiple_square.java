import java.io.*;
import java.util.*;
class GFG {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int a =sc.nextInt();
		int b =sc.nextInt();
		
		int f1=0;
		int f2=0;
		
		if( a%2 == 0)
		{
		    if(b%a==0)
		        f1=1;
		    if(b==a*a)
		        f2=1;
		        
		    if(f1==1 && f2==1)
		        System.out.println("The number is a square and multiple");
		    else if(f1==1 && f2==0)
		        System.out.println("The number is a multiple");
		    else
		        System.out.println("Its is not square or multiple");
		}
		else{
		    System.out.println("Not even");
		}
		
	}
}
