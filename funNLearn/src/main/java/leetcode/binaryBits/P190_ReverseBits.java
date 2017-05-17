/*
 * Reverse bits of a given 32 bits unsigned integer.
 * 
 * For example, given 
 * input 43261596 (represented in binary as 00000010100101000001111010011100), 
 * return 964176192 (represented in binary as 00111001011110000010100101000000).
 * 
 * Follow up:
 * If this function is called many times, how would you optimize it?
 * 
 * Related problem: Reverse Integer
 */

package leetcode.binaryBits;

import java.util.HashMap;
import java.util.Map;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class P190_ReverseBits {
	/*------------------------------------------- 
	 * for all bits get one at a time and then shift 
	 * -------------------------------------------
	 */
	public static int reverseBits_1(int n) {
		int result = 0;
		for (int i = 0; i < 32; i++) {
			result += n & 1;
			n >>>= 1; // CATCH: must do unsigned shift
			if (i < 31) // CATCH: for last digit, don't shift!
				result <<= 1;
		}
		return result;
	}

	/*
	 * We can divide an int into 4 bytes, and reverse each byte then combine
	 * into an int. For each byte, we can use cache to improve performance.
	 */
	private final static Map<Byte, Integer> cache = new HashMap<Byte, Integer>();

	public static int reverseBits_2(int n) {
		byte[] bytes = new byte[4];
		for (int i = 0; i < 4; i++)
			// convert int into 4 bytes
			bytes[i] = (byte) ((n >>> 8 * i) & 0xFF);
		int result = 0;
		for (int i = 0; i < 4; i++) {
			result += reverseByte(bytes[i]); // reverse per byte
			if (i < 3)
				result <<= 8;
		}
		return result;
	}

	private static int reverseByte(byte b) {
		Integer value = cache.get(b); // first look up from cache
		if (value != null)
			return value;
		value = 0;
		// reverse by bit
		for (int i = 0; i < 8; i++) {
			value += ((b >>> i) & 1);
			if (i < 7)
				value <<= 1;
		}
		cache.put(b, value);
		return value;
	}

	@Test
	public void test() {
		assertTrue("Test1", reverseBits_1(43261596) == 964176192);
		assertTrue("Test2", reverseBits_2(43261596) == 964176192);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P190_ReverseBits.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
