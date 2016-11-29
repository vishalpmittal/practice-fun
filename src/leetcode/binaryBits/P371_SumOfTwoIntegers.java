package leetcode.binaryBits;

/**
 * Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -
 * 
 * Example:
 * Given a = 1 and b = 2, return 3.
 */

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class P371_SumOfTwoIntegers {

    public int getSum(int a, int b) {
        
    	
    	return a+b;
    }
	
	
	//
	public static boolean problem_1(int n) {
		return false;
	}

	public static boolean problem(int n) {
		return problem_1(n);
	}

	public static void main(String[] args) {
		assertTrue("Test1", problem(94));
		assertFalse("Test2", problem(97));
		System.out.println("All Tests passed");
	}
}
