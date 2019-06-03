/**
 * Tag: math, bit
 * 
 * Given an array of integers, every element appears twice except for one. 
 * Find that single one.
 * 
 * Note:
 * Your algorithm should have a linear runtime complexity. 
 * Could you implement it without using extra memory?
 * 
 * Example 1: Input: [2,2,1], Output: 1
 * Example 2: Input: [4,1,2,1,2], Output: 4
 */

package leetcode.algorithms.P101_P200;
import static org.junit.Assert.assertTrue;

public class P136_SingleNumber {

	/**
	 * Solution 1: O(n) , Space (n) take a hash set, remove if number is
	 * present, and put in it if not present. At the end the length of the hash
	 * set should be 1 with needed number
	 */

	/**
	 * Solution 2: n Log(n) Sort the array traverse the array
	 */

	/**
	 * Solution 3: XOR -> O(n) and space 1 
	 * XOR operator is commutative; means:
	 * A^B=B^A 
	 * e.g, 5^43^10 = 10^43^5= 43^5^10 =36 
	 * So, XOR {2,1,4,5,2,4,1} one
	 * by one is same as XOR{2,2,4,4,1,1,5}; And since A^A=0, 
	 * so:
	 * ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5.
	 */
	public static int singleNumber(int[] nums) {
		int result = 0;
		for (int i = 0; i < nums.length; i++) {
			result ^= nums[i];
		}
		return result;
	}

	public static void main(String[] args) {
		assertTrue("Test1", singleNumber(new int[] { 2, 1, 4, 5, 2, 4, 1 }) == 5);
		assertTrue("Test2", singleNumber(new int[] { 2, 1, 4, 2, 4, 1 }) == 0);
		System.out.println("All Tests passed");
	}
}
