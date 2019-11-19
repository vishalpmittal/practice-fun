/**
 * Tag: list
 *
 * Given a stream of integers and a window size, calculate the moving 
 * average of all integers in the sliding window.
 * 
 * For example,
 * MovingAverage m = new MovingAverage(3);
 * m.next(1) = 1
 * m.next(10) = (1 + 10) / 2
 * m.next(3) = (1 + 10 + 3) / 3
 * m.next(5) = (10 + 3 + 5) / 3
 */

package leetcode.algorithms.P301_P400;

import static org.junit.Assert.assertTrue;

import java.util.LinkedList;
import java.util.Queue;

public class P346_MovingAverageFromDataStream {
	private double previousSum = 0.0;
	private int maxSize;
	private Queue<Integer> currentWindow;

	/** Initialize your data structure here. */
	public P346_MovingAverageFromDataStream(int size) {
		currentWindow = new LinkedList<Integer>();
		maxSize = size;
	}

	public double next(int val) {
		if (currentWindow.size() == maxSize) {
			previousSum -= currentWindow.remove();
		}

		previousSum += val;
		currentWindow.add(val);
		return previousSum / currentWindow.size();
	}

	public static void main(String[] args) {
		P346_MovingAverageFromDataStream obj = new P346_MovingAverageFromDataStream(3);
		assertTrue("Test1", obj.next(1) == 1);
		assertTrue("Test2", obj.next(10) == ((1 + 10) / 2.0));
		assertTrue("Test3", obj.next(3) == (1 + 10 + 3) / 3.0);
		assertTrue("Test4", obj.next(5) == (10 + 3 + 5) / 3.0);
		System.out.println("All Tests passed ");
	}
}
