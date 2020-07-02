/**
 * tag: string, diagram
 * 
 * We are given a string S consisting of N lowercase letters. A sequence of two 
 * adjacent letters inside a string is called a digram. The distance between two digrams 
 * is the distance between the first letter of the first digram and the first letter of the
 * second digram. 
 * For example, in string S = "akemz" the distance between digrams "kc" and "mz" is 2.
 * 
 * We want to find the distance between the furthest identical digrams inside string S.
 * 
 * given a string S consisting of N letters, returns the distance between the two 
 * identical digrams in the string that lie furthest away from each other. 
 * If there are no two identical digrams inside S, your function should return -1.
 * 
 * Examples:
 * 1. Given S = "aakmaakmakda" your function should return 7. The furthest identical
 * digrams are "ak"s, starting in positions 2 and 9 (enumerating from 1): "aakmaakmakda".
 * 2. Given S = "aaa" your function should return 1. 
 * The furthest identical digrams are "aa's starting at positions 1 and 2.
 * 3. Given S = "codility" your function should return -1. 
 * There are no two identical digrams in S.
 * 
 * Assumptions:
 * -  N is an integer within the range [2..300,000)];
 * -  string S consists only of lowercase letters (a-z).
 */

package dsAlgo.string;

import java.util.HashMap;

public class Digram {
    public int getDiagramLength(String S) {
        if (S.length() < 3)
            return -1;

        HashMap<String, Integer> low_index = new HashMap<String, Integer>();
        HashMap<String, Integer> high_index = new HashMap<String, Integer>();

        for (int i = 0; i < S.length() - 1; i++) {
            String curr_digram = S.substring(i, i + 2);

            if (!low_index.containsKey(curr_digram))
                low_index.put(curr_digram, i);
            else
                high_index.put(curr_digram, i);
        }

        int max_dist = -1;
        for (String key : high_index.keySet())
            max_dist = Math.max(max_dist, high_index.get(key) - low_index.get(key));

        return max_dist;
    }

    public static void main(String args[]) {
        Digram digram = new Digram();

        String[] input = { "aakmaakmakda", "aaa", "codility" };
        int[] output = { 7, 1, -1 };

        boolean passed = true;
        for (int i = 0; i < input.length; i++) {
            if (digram.getDiagramLength(input[i]) != output[i]) {
                System.out.printf("Failed test! Input: %s, Output: %s\n", input[i], output[i]);
                passed = false;
            }
        }
        if (passed)
            System.out.println("Tests Passed!");
    }
}