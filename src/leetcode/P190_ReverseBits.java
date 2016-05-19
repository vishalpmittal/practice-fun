/*
 * Reverse bits of a given 32 bits unsigned integer.
 * 
 * For example, given 
 *   input 43261596 (represented in binary as 00000010100101000001111010011100), 
 * return 964176192 (represented in binary as 00111001011110000010100101000000).
 * 
 * Follow up:
 * If this function is called many times, how would you optimize it?
 * 
 * Related problem: Reverse Integer
 */

package leetcode;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class P190_ReverseBits {
    public int reverseBits(int n) {
    	
    	return 0;
    }

	@Test
	public void test() {
//		assertTrue("Test1", problem(94));
//		assertFalse("Test2", problem(97));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P190_ReverseBits.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
