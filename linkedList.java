/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

public class Node
{    
    int data;    
    Node next;    
        
    public Node(int data)
    {    
        this.data = data;    
        this.next = null;    
    }    
} 

class LinkedList 
{    
    
    public Node head = null;    
    public Node tail = null;    
        
    public void addNode(int data) 
    {    
        Node value = new Node(data);    

        if(head == null) 
        {    
            head = value;    
            tail = value;    
        }    
        else 
        {    
            tail.next = value;    
            tail = value;    
        }    
    }    
        
    public void display() 
    {    
        Node cur = head;    
            
        System.out.println("Elements of the linked list are ");    
        while(cur != null) 
        {    
            System.out.print(cur.data + " ");    
            cur = cur.next;    
        }    
    }    
        
    public static void main(String[] args) {    
            
        LinkedList ll = new LinkedList();    
            
        ll.addNode(1);    
        ll.addNode(2);    
        ll.addNode(3);    
        ll.addNode(4);    
            
        ll.display();    
    }    
}
