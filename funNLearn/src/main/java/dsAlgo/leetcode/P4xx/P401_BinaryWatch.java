/**  
 * Tag: math, bit, recursive
 * 
 * A binary watch has 4 LEDs on the top which represent the hours (0-11), 
 * and the 6 LEDs on the bottom represent the minutes (0-59).
 * 
 * Each LED represents a zero or one, with the least significant bit on the right.
 * ----------------------------
 * |______8___4___2___1________|
 * |......0...0...1...1........|
 * |---------------------------|
 * |__32___16___8___4___2___1__|
 * |...0....1...1...0...0...1..|
 * ----------------------------
 * 
 * For example, the above binary watch reads "3:25".
 * 
 * Given a non-negative integer n which represents the number of LEDs that are 
 * currently on, return all possible times the watch could represent.
 * 
 * Example:
 * 
 * Input: n = 1
 * Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
 * 
 * Note:
 *  - The order of output does not matter.
 *  - The hour must not contain a leading zero, for example "01:00" is not valid, 
 *    it should be "1:00".
 *  - The minute must be consist of two digits and may contain a leading zero, for example "10:2" 
 *    is not valid, it should be "10:02".
 * --------------------------------------------- */

package dsAlgo.leetcode.P4xx;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class P401_BinaryWatch {

    /* ---------------------------------------------
     * go through the possible times and collect those with the
     * correct number of one-bits.
     * 
     * (h * 64 + m) is to differentiate hours and minutes by bit,
     * as hours will occupy 4 bits, and minutes will occupy 6.
     * --------------------------------------------- */
    public List<String> readBinaryWatch_1(int num) {
        List<String> times = new ArrayList<>();
        for (int h = 0; h < 12; h++)
            for (int m = 0; m < 60; m++)
                if (Integer.bitCount(h * 64 + m) == num)
                    times.add(String.format("%d:%02d", h, m));
        return times;
    }

    public static List<String> readBinaryWatch_2(int num) {
        List<String> res = new ArrayList<>();
        System.out.println("start         k         Choose");
        System.out.println("------------------------------");
        helper(res, new boolean[10], 0, num);
        return res;
    }

    static void helper(List<String> res, boolean[] choose, int start, int k) {
        // System.out.println("Choose: " + Arrays.toString(choose));
        System.out.println("  " + start + "         " + k + "        "
                + Arrays.toString(choose));
        if (k > 8)
            return;
        if (k == 0) {
            // (10 choose num) is done, check if time is valid
            int[] cache = new int[] { 8, 4, 2, 1, 32, 16, 8, 4, 2, 1 };
            int hh = 0, mm = 0;
            for (int i = 0; i < 10; i++) {
                if (choose[i]) {
                    if (i < 4)
                        hh += cache[i];
                    else
                        mm += cache[i];
                }
            }
            if (hh < 12 && mm < 60) {
                if (mm < 10)
                    res.add("" + hh + ":0" + mm);
                else
                    res.add("" + hh + ":" + mm);
            }
        } else {
            for (int i = start; i < choose.length - k + 1; i++) {
                choose[i] = true;
                helper(res, choose, i + 1, k - 1);
                choose[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        readBinaryWatch_2(3);
        // assertTrue("Test1", problem(94));
        // assertFalse("Test2", problem(97));
        System.out.println("All Tests passed");
    }
}
