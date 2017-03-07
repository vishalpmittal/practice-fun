package ocpjp.examples;

public class StringBuilderTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String str = "abc";
		
		long startTime = System.currentTimeMillis();
		for(int i=0;i<100000;i++)
		{
			str+="123";
		}
		long endTime = System.currentTimeMillis();
		
		System.out.println("String concat time: " + (endTime - startTime));
		
		
		StringBuilder sb = new StringBuilder("abc");
		startTime = System.currentTimeMillis();
		for(int i=0;i<100000;i++)
		{
			sb.append("123");
		}
		String st = sb.toString();
		endTime = System.currentTimeMillis();
		
		System.out.println("StringBuilder time: " + (endTime - startTime));
		

	}

}
