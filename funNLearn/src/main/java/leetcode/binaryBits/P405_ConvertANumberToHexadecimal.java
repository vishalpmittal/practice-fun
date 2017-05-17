package leetcode.binaryBits;

/** ---------------------------------------------
 * Given an integer, write an algorithm to convert it to hexadecimal. 
 * For negative integer, two’s complement method is used.
 * 
 * Note:
 * 
 * 1. All letters in hexadecimal (a-f) must be in lowercase.
 * 2. The hexadecimal string must not contain extra leading 0s. 
 * ...If the number is zero, it is represented by a single zero character '0'; 
 * ...otherwise, the first character in the hexadecimal string will not be the zero character.
 * 3. The given number is guaranteed to fit within the range of a 32-bit signed integer.
 * 4. You must not use any method provided by the library which converts/formats 
 * ...the number to hex directly.
 * 
 * Example 1:  
 * Input: 26;  Output: "1a"
 * 
 * Example 2:
 * Input: -1;  Output: "ffffffff"
 * --------------------------------------------- */

import static org.junit.Assert.assertTrue;

public class P405_ConvertANumberToHexadecimal {

    /* ---------------------------------------------
     * Basic idea: each time we take a look at the last four digits of
     * binary verion of the input, and maps that to a hex char
     * shift the input to the right by 4 bits, do it again
     * until input becomes 0.
     * --------------------------------------------- */
    public static String toHex(int num) {
        if (num == 0)
            return "0";
        StringBuilder sb = new StringBuilder();
        char[] hex = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a',
                'b', 'c', 'd', 'e', 'f' };
        while (num != 0) {
            sb.insert(0, hex[(num & 15)]);
            num = (num >>> 4);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        assertTrue("Test1", toHex(26).compareTo("1a") == 0);
        assertTrue("Test1", toHex(-1).compareTo("ffffffff") == 0);
        System.out.println("All Tests passed");
    }
}
