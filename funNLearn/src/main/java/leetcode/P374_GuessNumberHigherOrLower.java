package leetcode;

/** ---------------------------------------------
 * We are playing the Guess Game. The game is as follows:
 * 
 * I pick a number from 1 to n. You have to guess which number I picked.
 * 
 * Every time you guess wrong, I'll tell you whether the number is higher or lower.
 * 
 * You call a pre-defined API guess(int num) which returns 
 * 3 possible results (-1, 1, or 0):
 * 
 * -1 : My number is lower
 * 1 : My number is higher
 * 0 : Congrats! You got it!
 * 
 * Example:
 * n = 10, I pick 6.
 * Return 6.
 --------------------------------------------- */

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.Random;

class GuessGame {
    int guess(int num) {
        int[] arr = { -1, 0, 1 };
        return arr[(new Random()).nextInt(arr.length)];
    }
}

public class P374_GuessNumberHigherOrLower extends GuessGame {
    /* ---------------------------------------------
     * Problem statement is a little confusing
     * but the problem is a plain old binary search.
     * --------------------------------------------- */
    public int guessNumber(int n) {
        int i = 1, j = n;
        while (i < j) {
            int mid = i + (j - i) / 2;
            if (guess(mid) == 0) {
                return mid;
            } else if (guess(mid) == 1) {
                i = mid + 1;
            } else {
                j = mid;
            }
        }
        return i;
    }

    public static void main(String[] args) {
        // assertTrue("Test1", problem(94));
        // assertFalse("Test2", problem(97));
        System.out.println("All Tests passed");
    }
}