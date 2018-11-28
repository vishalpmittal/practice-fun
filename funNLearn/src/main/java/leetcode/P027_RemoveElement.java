/*
 * Given an array and a value, remove all instances of that value in place and return the new length.
 * Do not allocate extra space for another array, you must do this in place with constant memory.
 * The order of elements can be changed. It doesn't matter what you leave beyond the new length.
 * 
 * Example:
 * Given input array nums = [3,2,2,3], val = 3
 * 
 * Your function should return length = 2, with the first two elements of nums being 2.
 */

package leetcode;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;

public class P027_RemoveElement {
	// Using two pointers iterative
	public static int removeElement_1(int[] nums, int val) {
		int m = 0;
		for (int i = 0; i < nums.length; i++) {

			if (nums[i] != val) {
				nums[m] = nums[i];
				m++;
			}
		}
		int retVal = m;

		while (m < nums.length) {
			nums[m] = -1;
			m++;
		}

		return retVal;
	}

	// Using front and back pointer
	public static int removeElement_2(int[] nums, int val) {
		int start = 0, end = nums.length - 1;
		while (start <= end) {
			if (nums[start] == val) {
				if (nums[end] == val)
					end--;
				else {
					nums[start] = nums[end];
					start++;
					end--;
				}
			} else {
				start++;
			}
		}
		return start;
	}

	public static int removeElement(int[] nums, int val) {
		return removeElement_1(nums, val);
	}

	@Test
	public void test() {
		int[] testArr = { 1, 2, 3, 4, 5 };
		int[] arr = { 3, 2, 2, 3 };

		assertTrue("Test1", removeElement(testArr, 3) == 4);
		assertTrue("Test2", removeElement(arr, 3) == 2);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P027_RemoveElement.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
