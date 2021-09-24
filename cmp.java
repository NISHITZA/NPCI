import java.io.*;
import java.util.*;

class User{

    int userId;
    String name;

    User(int id,String uName){
        userId = id;
        name = uName;
    }

   @Override
    public String toString() {
        return "User => Id =" + userId +", Name = "+name;
    }

}

public class SortById implements Comparator<User> {

    @Override
    public int compare(User o1, User o2) {
        return o1.userId - o2.userId;
    }
}

public class SortByName implements Comparator<User> {
    @Override
    public int compare(User o1, User o2) {
        return o2.name.compareTo(o1.name);
    }
}


class GFG
{
	public static void main (String[] args) 
	{
		ArrayList<User> ar = new ArrayList<User>();
		User o1 = new User(05, "Kody");
		User o2 = new User(02, "Nish");
		User o3 = new User(01, "Mi");
		
		ar.add(o1);
		ar.add(o2);
		ar.add(o3);
		
		Collections.sort(ar, new SortById());
		
		for (int i = 0; i < ar.size(); i++)
            System.out.println(ar.get(i));
		
	}
}
