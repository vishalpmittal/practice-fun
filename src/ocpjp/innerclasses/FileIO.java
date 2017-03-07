package ocpjp.innerclasses;

import java.io.FileNotFoundException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class FileIO {

	/**
	 * @param args
	 * @throws FileNotFoundException 
	 */
	public static void main(String[] args) throws FileNotFoundException {
		Pattern regexPattern = Pattern.compile("a");
		
		String str = "aabbbbjyriurhfraajslkakipokf";
		
		
		Matcher m = regexPattern.matcher(str);
		
		while(m.find())
		{
			System.out.println(m.start());
		}
	}

}
