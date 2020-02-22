/** 
 * Tag: math
 * 
 * Find the total area covered by two rectilinear rectangles in a 2D plane.
 * Each rectangle is defined by its bottom left corner and top right corner as 
 * shown in the figure.
 * Assume that the total area is never beyond the maximum possible value of int.
 * 
 * Example:
 * Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
 * Output: 45
 * 
 */

package dsAlgo.leetcode.P2xx;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P223_RectangleArea {

	public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
		int areaOfSqrA = (C - A) * (D - B);
		int areaOfSqrB = (G - E) * (H - F);

		int left = Math.max(A, E);
		int right = Math.min(G, C);
		int bottom = Math.max(F, B);
		int top = Math.min(D, H);

		//If overlap
		int overlap = 0;
		if (right > left && top > bottom)
			overlap = (right - left) * (top - bottom);

		return areaOfSqrA + areaOfSqrB - overlap;
	}

	@Test
	public void test() {
		assertTrue("Test1", computeArea(1, 2, 3, 4, 5, 6, 7, 8) == 8);
		assertTrue("Test1", computeArea(1, 1, 2, 2, 5, 5, 7, 7) == 5);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P223_RectangleArea.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
