/**
 * Tag: math
 *
 * Write a program to check whether a given number is an ugly number.
 * Ugly numbers are positive numbers whose prime factors only include 
 * 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it 
 * includes another prime factor 7.
 * 
 * Note that 1 is typically treated as an ugly number.
 */
package leetcode.algorithms.P2xx;

public class P263_UglyNumber {

	/*
	 * Long and lengthy solution
	 * find out all the factors and as soon as any factor is not 2 3 or 5
	 * return false;
	 */
	public static boolean isUgly(int num) {
		if (num <= 0)
			return false;
		while (num > 1) {
			for (int i = 2; i <= num; i++) {
				if (num % i == 0) {
					if (i != 2 && i != 3 && i != 5)
						return false;
					num = num / i;
					break;
				}
			}
		}
		return true;
	}

	/* 
	 * Faster solution
	 * Just divide the number by 2 3 4  and 5 and if the number becomes 1
	 * return true
	 */
	public static boolean isUgly_1(int num) {
		for (int i = 2; i < 6 && num > 0; i++)
			while (num % i == 0)
				num /= i;
		return num == 1;
	}
	
	/*
	 * Recursive solution
	 * idea:
	 * (1) basic cases: <= 0 and == 1
	 * (2) other cases: since the number can contain the factors of 2, 3, 5, I just 
	 * remove those factors. So now, I have a number without any factors of 2, 3, 5.
	 * (3) after the removing, the number (new number) can contain a) the factor that 
	 * is prime and meanwhile it is >= 7, or b) the factor that is not the prime and 
	 * the factor is not comprised of 2, 3 or 5. In both cases, 
	 * it is false (not ugly number).
	 * 
	 */
	public static boolean isUgly_2(int num) {
	    if (num <= 0) {return false;}
	    if (num == 1) {return true;}
	    if (num % 2 == 0) {
	        return isUgly(num/2);
	    }
	    if (num % 3 == 0) {
	        return isUgly(num/3);
	    }
	    if (num % 5 == 0) {
	        return isUgly(num/5);
	    }
	    return false;
	}
		
	public static void main(String[] args) {
		System.out.println(isUgly(905391974));
	}

}
