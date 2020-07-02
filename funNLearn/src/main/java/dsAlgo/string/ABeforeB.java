/**
 * tag: string
 * 
 * Write a function solution that, given a string S consisting of N letters
 *  "a" and/or "b" returns true when all occurrences of letter "a" are before 
 * all occurrences of letter "b" and returns false otherwise.
 * 
 * Examples:
 * 1. Given S = "aabbb", the function should return true.
 * 2. Given S = "ba", the function should return false.
 * 3. Given S = "aaa", the function should return true. Note that "b" does not need to occur in S
 * 4. Given S = "b", the function should return true. Note that "a" does not need to occur in S
 * 5. Given S = "abba", the function should return false.
 * 
 * Assumptions:
 * - N is an integer within the range [1..300,000);
 * - string S consists only of the characters "a" and/or "b".
 */

package dsAlgo.string;

public class ABeforeB {
    public boolean areAllAsBeforeBs(String S) {
        if (S.length() < 2)
            return true;

        int max_a = -1;
        int max_b = -1;
        boolean found_b = false;

        for (int i = 0; i < S.length(); i++) {
            if (Character.compare(S.charAt(i), 'a') == 0)
                max_a = Math.max(i, max_a);

            else if (Character.compare(S.charAt(i), 'b') == 0) {
                found_b = true;
                max_b = Math.max(i, max_b);
            }

            if (found_b && max_a > max_b)
                return false;
        }

        return true;
    }

    public static void main(String args[]) {
        ABeforeB abb = new ABeforeB();

        String[] input = { "aabbb", "ba", "aaa", "b", "abba" };
        boolean[] output = { true, false, true, true, false };

        boolean passed = true;
        for (int i = 0; i < input.length; i++) {
            if (abb.areAllAsBeforeBs(input[i]) != output[i])
                System.out.printf("Failed test! Input: %s, Output: %s", input[i], output[i]);
        }
        if (passed)
            System.out.println("Tests Passed!");
    }
}
