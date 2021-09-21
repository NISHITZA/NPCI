/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;
class GFG {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int a =sc.nextInt();
		
		int count =0;
		
		int b=a;
		
		while(a>0){
		    count ++;
		    a=a/10;
		}
		
		System.out.println(count);
		int value;
		int flag=0;
		if(count%3==0){
		   value=count*count*count;
		   flag=1;
		}
		else if(count%2==0){
		   value=count*count;
		}
		else{
		    int temp=count-1;
		    value=temp*temp;
		}
		System.out.println("The count is "+count);
		if(count==1){
		//    System.out.println("The count is one");
		}
		else if(flag==1)
		    System.out.println("The cube is "+value);
		else
		    System.out.println("The square is "+value);
	}
}
