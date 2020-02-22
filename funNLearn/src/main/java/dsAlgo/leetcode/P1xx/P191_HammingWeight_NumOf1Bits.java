/**
 * Tag: bit
 *
 * Write a function that takes an unsigned integer and returns the number 
 * of ’1' bits it has (also known as the Hamming weight).
 * 
 * For example, the 32-bit integer ’11' has binary 
 * representation 00000000000000000000000000001011, so the function should return 3.
 * 
 */

package dsAlgo.leetcode.P1xx;

public class P191_HammingWeight_NumOf1Bits {

	// you need to treat n as an unsigned value
	public static int hammingWeight(int n) {
		String str = Integer.toBinaryString(n);
		int ones = 0;
		for (int i = 0; i < str.length(); i++)
			ones = str.charAt(i) == '1' ? ones + 1 : ones;
		return ones;
	}

	/**
	 * An Integer in Java has 32 bits, e.g. 00101000011110010100001000011010. To
	 * count the 1s in the Integer representation with put the input int n in bit
	 * AND with 1 (that is represented as 00000000000000000000000000000001, and if
	 * this operation result is 1, that means that the last bit of the input integer
	 * is 1. Thus we add it to the 1s count. ones = ones + (n & 1);
	 * 
	 * Then we shift the input Integer by one on the right, to check for the next
	 * bit. n = n>>>1;
	 * 
	 * We need to use bit shifting unsigned operation >>> (while >> depends on sign
	 * extension)
	 * 
	 * We keep doing this until the input Integer is 0. In Java we need to put
	 * attention on the fact that the maximum integer is 2147483647. Integer type in
	 * Java is signed and there is no unsigned int. So the input 2147483648 is
	 * represented in Java as -2147483648 (in java int type has a cyclic
	 * representation, that means Integer.MAXVALUE+1==Integer.MINVALUE). This force
	 * us to use n!=0 in the while condition and we cannot use n>0 because the input
	 * 2147483648 would correspond to -2147483648 in java and the code would not
	 * enter the while if the condition is n>0 for n=2147483648.
	 */
	public static int hammingWeight_1(int n) {
		int ones = 0;
		while (n != 0) {
			ones = ones + (n & 1);
			n = n >>> 1;
		}
		return ones;
	}

	public static void main(String[] args) {
		System.out.println(Integer.toBinaryString(355));
		System.out.println(hammingWeight(355));

	}

}
