package java.exceptions;

public class DivideByZeroException extends Exception{
	
	private static final long serialVersionUID = 1L;
	
	String err_msg;
	
	DivideByZeroException(){
		err_msg = new String("Your second string is 0: NOT Allowed :P");
	}
	
	public boolean validate_num(int a){
		if(a==0)
			return true;
		else 
			return false;
	}
}
