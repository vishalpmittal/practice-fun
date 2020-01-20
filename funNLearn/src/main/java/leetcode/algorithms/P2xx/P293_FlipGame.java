/**
 * Tag: array
 * 
 * You are playing the following Flip Game with your friend: Given a 
 * string that contains only these two characters: + and -, you and 
 * your friend take turns to flip two consecutive "++" into "--". 
 * The game ends when a person can no longer make a move and therefore 
 * the other person will be the winner.
 * 
 * Write a function to compute all possible states of the string after 
 * one valid move.
 * 
 * For example, 
 * given s = "++++", after one move, it may become one of the following states:
 * 
 * [
 *   "--++",
 *   "+--+",
 *   "++--"
 * ]
 * 
 * If there is no valid move, return an empty list [].
 */

package leetcode.algorithms.P2xx;

import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.List;

public class P293_FlipGame {
	public static List<String> generatePossibleNextMoves(String s) {
		List<String> moves = new ArrayList<String>();
		if (s == null || s.length() < 2)
			return moves;

		for (int i = 0; i < s.length() - 1; i++) {
			if (s.charAt(i) == '+' && s.charAt(i + 1) == '+') {
				moves.add(s.substring(0, i) + "--" + s.substring(i + 2));
			}
		}
		return moves;
	}

	public static void main(String[] args) {
		assertTrue("Test1", generatePossibleNextMoves(null).isEmpty());
		assertTrue("Test2", generatePossibleNextMoves("").isEmpty());
		assertTrue("Test3", generatePossibleNextMoves("-").isEmpty());
		assertTrue("Test4", generatePossibleNextMoves("+").isEmpty());
		assertTrue("Test5", generatePossibleNextMoves("--").isEmpty());
		assertTrue("Test6", generatePossibleNextMoves("-+").isEmpty());
		assertTrue("Test6", generatePossibleNextMoves("++").size() == 1);
		assertTrue("Test6", generatePossibleNextMoves("++++").size() == 3);
		assertTrue("Test7", generatePossibleNextMoves("12345").isEmpty());

		System.out.println("All Tests passed");
	}
}
