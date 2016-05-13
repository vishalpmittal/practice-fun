/*
* Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
* http://sudoku.com.au/TheRules.aspx
* 
* The Sudoku board could be partially filled, 
* where empty cells are filled with the character '.'.
* 
* A partially filled sudoku which is valid.
* |----------------------------------|
* |  5  3  .  | .  7  .  |  .  .  .  |
* |  6  .  .  | 1  9  5  |  .  .  .  |
* |  .  9  8  | .  .  .  |  .  6  .  |
* |----------------------------------|
* |  8  .  .  | .  6  .  |  .  .  3  |
* |  4  .  .  | 8  .  3  |  .  .  1  |
* |  7  .  .  | .  2  .  |  .  .  6  |
* |----------------------------------|
* |  .  6  .  | .  .  .  |  2  8  .  |
* |  .  .  .  | 4  1  9  |  .  .  5  |
* |  .  .  .  | .  8  .  |  .  7  9  |
* |----------------------------------|
* 
* Note:
* A valid Sudoku board (partially filled) is not necessarily solvable. 
* Only the filled cells need to be validated.
*/

package leetcode;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class P036_ValidSudoku {
	// Solution 1: hashmap of hashsets solution
	public static boolean isValidSudoku(char[][] board) {
		HashMap<Integer, HashSet<Character>> validator = new HashMap<Integer, HashSet<Character>>();

		for (int row = 0; row < 9; row++) {
			for (int col = 0; col < 9; col++) {
				int currCol = 10 + col;
				int currQuad = 20 + (((row / 3) * 3) + (col / 3));
				Character currChar = board[row][col];

				if (currChar == '.') {
					continue;
				}
				if (validator.get(row) == null)
					validator.put(row, new HashSet<Character>());

				if (validator.get(currCol) == null)
					validator.put(currCol, new HashSet<Character>());

				if (validator.get(currQuad) == null)
					validator.put(currQuad, new HashSet<Character>());

				if (!validator.get(row).add(currChar) || !validator.get(currCol).add(currChar)
						|| !validator.get(currQuad).add(currChar))
					return false;
			}
		}
		return true;
	}

	// Solution 2: Single hashset solution
	// 5 th row number 2 = 52
	// 5 th col number 2 = 152
	// 5 th quadrant number 2 = 252
	public static boolean isValidSudoku_1(char[][] board) {
		HashSet<Integer> validator = new HashSet<Integer>();
		for (int row = 0; row < 9; row++) {
			for (int col = 0; col < 9; col++) {
				if (board[row][col] == '.') {
					continue;
				}
				
				int currNum = (int) board[row][col];
				int currRow = (10 * row) + currNum;
				int currCol = 100 + (10 * col) + currNum;
				int currQuad = 200 + (10 * (((row / 3) * 3) + (col / 3))) + currNum;

				if (!validator.add(currRow) || !validator.add(currCol) || !validator.add(currQuad))
					return false;
			}
		}
		return true;
	}

	// Solution 3: Each time send the coordinates to check if the board is partially valid.
	public boolean isValidSudoku_2(char[][] board) {
		for (int i = 0; i < 9; i++) {
			if (!isParticallyValid(board, i, 0, i, 8))
				return false;
			if (!isParticallyValid(board, 0, i, 8, i))
				return false;
		}
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (!isParticallyValid(board, i * 3, j * 3, i * 3 + 2, j * 3 + 2))
					return false;
			}
		}
		return true;
	}

	private boolean isParticallyValid(char[][] board, int x1, int y1, int x2, int y2) {
		Set<Character> singleSet = new HashSet<Character>();
		for (int i = x1; i <= x2; i++) {
			for (int j = y1; j <= y2; j++) {
				if (board[i][j] != '.')
					if (!singleSet.add(board[i][j]))
						return false;
			}
		}
		return true;
	}

	@Test
	public void test() {
		char[] line0 = { '5', '3', '.', '.', '7', '.', '.', '.', '.' };
		char[] line1 = { '6', '.', '.', '1', '9', '5', '.', '.', '.' };
		char[] line2 = { '.', '9', '8', '.', '.', '.', '.', '6', '.' };
		char[] line3 = { '8', '.', '.', '.', '6', '.', '.', '.', '3' };
		char[] line4 = { '4', '.', '.', '8', '.', '3', '.', '.', '1' };
		char[] line5 = { '7', '.', '.', '.', '2', '.', '.', '.', '6' };
		char[] line6 = { '.', '6', '.', '.', '.', '.', '2', '8', '.' };
		char[] line7 = { '.', '.', '.', '4', '1', '9', '.', '.', '5' };
		char[] line8 = { '.', '.', '.', '.', '8', '.', '.', '7', '9' };

		char[][] board = { line0, line1, line2, line3, line4, line5, line6, line7, line8 };

		assertTrue("Test1", isValidSudoku_1(board));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P036_ValidSudoku.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
