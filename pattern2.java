/*package whatever //do not write package name here */

import java.io.*;

class GFG {
	public static void main (String[] args) {
	    
	    int sum =1;
	    int final_sum=0;
	    for(int i=0; i<4;i++){
	        
	        for(int j=0;j<=i;j++){
	            
	            for(int k=4-i; k>0; k--)
	                System.out.print(" ");
	            
	            System.out.print(sum+" ");
	            final_sum = final_sum + sum;
	        }
	        if(i==0)
	            sum=2;
	        else
	            sum=final_sum;
	        System.out.println("");
		}
	}
}
