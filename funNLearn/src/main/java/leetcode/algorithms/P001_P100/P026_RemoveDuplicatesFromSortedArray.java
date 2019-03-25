/**
 * Tag: array
 * 
 * Given a sorted array, remove the duplicates in place such that each 
 * element appear only once and return the new length.
 * 
 * Do not allocate extra space for another array, 
 * you must do this in place with constant memory.
 * 
 * For example,
 * Given input array nums = [1,1,2],
 * 
 * Your function should return length = 2, with the first two elements of 
 * nums being 1 and 2 respectively. 
 * It doesn't matter what you leave beyond the new length.
 * 
 */

package leetcode.algorithms.P001_P100;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;

import java.util.Arrays;

public class P026_RemoveDuplicatesFromSortedArray {
	// start two pointers at the beginning. 
	// if duplicate found keep incrementing i but if no duplicate found 
	// copy the integer to last unique index lui+1 and increment lui
	public int removeDuplicates(int[] nums) {
		int len = nums.length;
		if (len < 2)
			return len;

		int lui = 0;
		for (int i = 0; i < len - 1; i++) {
			if (nums[i] != nums[i + 1]) {
				nums[lui + 1] = nums[i + 1];
				lui++;
			}
		}
		return ++lui;
	}

	@Test
	public void test() {
		int[] nums1 = { 1, 2, 2, 2, 3, 4, 5 };
		int[] nums2 = { 1, 1, 2 };

		assertTrue("Test1", removeDuplicates(nums1) == 5);
		System.out.println(Arrays.toString(nums1));
		assertTrue("Test1", removeDuplicates(nums2) == 2);
		System.out.println(Arrays.toString(nums2));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P026_RemoveDuplicatesFromSortedArray.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
