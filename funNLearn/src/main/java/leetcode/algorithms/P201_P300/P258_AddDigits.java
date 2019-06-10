/**
 * Tag: math
 * 
 * Given a non-negative integer num, repeatedly add all its digits 
 * until the result has only one digit.
 * For example:
 * Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. 
 * Since 2 has only one digit, return it.
 * 
 * Follow up:
 * 	Could you do it without any loop/recursion in O(1) runtime?
 * 
 * 
 * Wikipedia Article 
 * https://en.wikipedia.org/wiki/Digital_root
 * Digital Root (AKA Repeated Digital Sum) 
 */

package leetcode.algorithms.P201_P300;

public class P258_AddDigits {

	public static int addDigits(int num) {
		int sum = Integer.MAX_VALUE;
		int tempNum = num; 
		
		while (sum >= 10){
			sum = 0;
			int countNum = tempNum;
			while (countNum > 0){
				sum += countNum%10;
				countNum = countNum/10;
			}
			tempNum = sum;
		}
		return sum;
	}

	// O(1)
	// Find the nearest multiplier of 9 lower than num
	// then subtract it from the num
	// eg: nearest multiplier of 9 lower than num 78 is 72
	// thus we do 78-72 = 6, which is the answer
	public static int addDigits1(int num) {
		return (num-(9*((num-1)/9)));
	}
	
	public static void main(String[] args) {
		System.out.println(addDigits1(45));
	}
}
