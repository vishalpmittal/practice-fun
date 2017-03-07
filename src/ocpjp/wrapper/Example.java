package ocpjp.wrapper;

import java.util.ArrayList;
import java.util.List;

public class Example {

	
	//primitive type -> wrapper class object   (Wrapper class constructor)
	//wrapper class object -> primitive type value   (  .XXXvalue())
	
	
	
	//primitive type -> wrapper object  -> Boxing
	//wrapper object -> primitive type  -> Unboxing
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int a = 45;
		int b = 55;
		
		Integer result = new Integer(add(a,b));
		int r = result;
		
		List<Integer> li = new ArrayList<Integer>();
		li.add(6);

	}
	
	
	public static int add(Integer a, Integer b)
	{
		int result = a + b;
		return result;
	}

}
