/** 
 * Tag: string
 * ---------------------------------------------
 * Given an arbitrary ransom note string and another string containing 
 * letters from all the magazines, write a function that will return true 
 * if the ransom note can be constructed from the magazines ; 
 * otherwise, it will return false.
 * 
 * Each letter in the magazine string can only be used once in your ransom note.
 * 
 * Note:
 * You may assume that both strings contain only lowercase letters.
 * 
 * canConstruct("a", "b") -> false
 * canConstruct("aa", "ab") -> false
 * canConstruct("aa", "aab") -> true
 --------------------------------------------- */

 package leetcode.algorithms.P301_P400;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class P383_RansomNote {
    /* ---------------------------------------------
     * O(n) solution
     * --------------------------------------------- */
    public static boolean canConstruct(String ransomNote, String magazine) {
        int[] arr = new int[26];
        for (int i = 0; i < magazine.length(); i++) {
            arr[magazine.charAt(i) - 'a']++;
        }
        for (int i = 0; i < ransomNote.length(); i++) {
            if (--arr[ransomNote.charAt(i) - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        assertTrue("Test1", canConstruct("aa", "aab"));
        assertTrue("Test2", canConstruct("aabcb", "xyzacbba"));
        assertFalse("Test3", canConstruct("aa", "ab"));
        System.out.println("All Tests passed");
    }
}
