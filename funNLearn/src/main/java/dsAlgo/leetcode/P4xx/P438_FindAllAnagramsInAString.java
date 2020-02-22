/*
 * Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
 * 
 * Strings consists of lowercase English letters only and the length of both strings s and p 
 * will not be larger than 20,100.
 * 
 * The order of output does not matter.
 * 
 * Example 1:
 * -------------------
 * Input:
 * s: "cbaebabacd" p: "abc"
 * 
 * Output:
 * [0, 6]
 * 
 * Explanation:
 * The substring with start index = 0 is "cba", which is an anagram of "abc".
 * The substring with start index = 6 is "bac", which is an anagram of "abc".
 * 
 * Example 2:
 * -------------------
 * Input:
 * s: "abab" p: "ab"
 * 
 * Output:
 * [0, 1, 2]
 * 
 * Explanation:
 * The substring with start index = 0 is "ab", which is an anagram of "ab".
 * The substring with start index = 1 is "ba", which is an anagram of "ab".
 * The substring with start index = 2 is "ab", which is an anagram of "ab".
 */

package dsAlgo.leetcode.P4xx;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class P438_FindAllAnagramsInAString {

    public List<Integer> findAnagrams(String s, String p) {
        if (s == null || p == null || s.isEmpty() || p.isEmpty() || s.length() < p.length())
            return new ArrayList<Integer>();

        Map<Character, Integer> anaStr = new HashMap<Character, Integer>();
        s.chars().forEach(c -> {
            char c_char = (char) c;
            if (anaStr.containsKey(c_char))
                anaStr.put(c_char, anaStr.get(c_char) + 1);
            else
                anaStr.put(c_char, 1);
        });

        return null;
    }

    public static void main(String[] args) {
        // assertTrue("Test1", missingNumber(arr1) == 2);
        // assertTrue("Test2", missingNumber(arr2) == 8);
        System.out.println("All Tests passed");
    }
}
