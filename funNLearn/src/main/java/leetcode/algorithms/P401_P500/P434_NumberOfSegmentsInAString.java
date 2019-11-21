/** 
 * Tag: string
 * 
 * ---------------------------------------------
 * Count the number of segments in a string, where a segment is defined to 
 * be a contiguous sequence of non-space characters.
 * 
 * Please note that the string does not contain any non-printable characters.
 * 
 * Example:
 * Input: "Hello, my name is John"
 * Output: 5
 * --------------------------------------------- */

package leetcode.algorithms.P401_P500;

import static org.junit.Assert.assertTrue;

public class P434_NumberOfSegmentsInAString {

    public static int countSegments(String s) {
        int res = 0;
        for (int i = 0; i < s.length(); i++)
            if (s.charAt(i) != ' ' && (i == 0 || s.charAt(i - 1) == ' '))
                res++;
        return res;
    }

    public static void main(String[] args) {
        assertTrue("Test1", countSegments("Hello, my name is John") == 5);
        System.out.println("All Tests passed");
    }
}
