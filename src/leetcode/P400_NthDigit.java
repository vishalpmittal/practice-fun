package leetcode;

/** ---------------------------------------------
 * Find the nth digit of the infinite integer sequence 
 * 
 * 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
 * 
 * Note:
 * n is positive and will fit within the range of a 32-bit signed integer (n < 2 to power 31).
 * 
 * Example 1:
 * Input: 3
 * Output: 3
 * 
 * Example 2:
 * Input: 11
 * Output: 0
 * 
 * Explanation:
 * The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, 
 * which is part of the number 10.
 * --------------------------------------------- */

import static org.junit.Assert.assertTrue;

public class P400_NthDigit {

    /* ---------------------------------------------
     * 1~9: 1*9=9 in total
     * 10~99: 2*90=180 in total
     * 100~999: 3*900=2700 in total
     * Then, 4 * 9000, 5 * 90000, k * 9 * 10^k-1
     * 
     * For input 12345
     * len
     * len = 1, count = 9, start = 1, n = 12345
     * len = 1, count = 9, start = 1, n = 12336
     * len = 2, count = 90, start = 10, n = 12336
     * len = 2, count = 90, start = 10, n = 12156
     * len = 3, count = 900, start = 100, n = 12156
     * len = 3, count = 900, start = 100, n = 9456
     * len = 4, count = 9000, start = 1000, n = 9456
     * 
     * start = 1000 + (9456 - 1) / 4 = 3363
     * s = 3363
     * index = (9456 - 1) % 4 = 3
     * return 3363.charAt(3) = 3
     * 
     * Straight forward way to solve the problem in 3 steps:
     * 
     * - find the length of the number where the nth digit is from
     * - find the actual number where the nth digit is from
     * - find the nth digit and return
     * --------------------------------------------- */
    public static int findNthDigit_1(int n) {
        int len = 1;
        long count = 9;
        int start = 1;

        while (n > len * count) {
            n -= len * count;
            len += 1;
            count *= 10;
            start *= 10;
        }

        start += (n - 1) / len;
        String s = Integer.toString(start);
        int index = (n - 1) % len;
        return Character.getNumericValue(s.charAt(index));
    }

    /* ---------------------------------------------
     * YAI : pre-stored checkpoints.
     * ---------------------------------------------
     * a little faster
     * --------------------------------------------- */
    public int findNthDigit(int n) {
        int[] digitInd = { 1, 10, 190, 2_890, 38_890, 488_890, 5_888_890,
                68_888_890, 788_888_890 };
        int[] nums = { 1, 10, 100, 1_000, 10_000, 100_000, 1_000_000,
                10_000_000, 100_000_000 };
        int i;
        for (i = 0; i < digitInd.length - 1 && digitInd[i + 1] <= n; i++)
            ;
        int digitNum = i + 1;
        int offset = n - digitInd[i];
        int num = nums[i] + offset / digitNum;
        offset %= digitNum;
        for (n = digitNum - offset - 1; n > 0; n--, num /= 10)
            ;
        return num % 10;
    }

    public static void main(String[] args) {
        assertTrue("Test1", findNthDigit_1(12345) == 3);
        System.out.println("All Tests passed");
    }
}
