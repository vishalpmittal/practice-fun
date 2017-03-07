package ocpjp.unit1;

import java.util.ArrayList;
import java.util.List;

public class Test {
	
	
	public static void main(String [] args)
	{
		int val = 100;
		m1(val);    //Boxing   -> m1(new Integer(val));
		
		Integer i1 = new Integer(800);
		m2(i1);     //Unboxing   -> m2(i1.intValue());
		
		
		
		
		List<Integer> li = new ArrayList<Integer>();
		li.add(new Integer(6));
	}
	public static void m1(Integer m1)
	{
		
	}
	
	public static void m2(int val)
	{
		
	}
}


