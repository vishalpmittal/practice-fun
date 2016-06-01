/*
* Rotate an array of n elements to the right by k steps.
* 
* For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
* 
* Note:
* Try to come up as many solutions as you can, there are at least 
* 3 different ways to solve this problem.
* 
* Hint:
* Could you do it in-place with O(1) extra space?
* Related problem: Reverse Words in a String II
*/

package leetcode.lists;

import static org.junit.Assert.assertTrue;

import java.util.Arrays;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P189_RotateArray {
	/*
	 * The basic idea is that, for example, nums = [1,2,3,4,5,6,7] and k = 3, 
	 * first we reverse [1,2,3,4], it becomes[4,3,2,1]; then we reverse[5,6,7], 
	 * it becomes[7,6,5], finally we reverse the array as a whole, 
	 * it becomes[4,3,2,1,7,6,5] ---> [5,6,7,1,2,3,4].
	 * 
	 * Reverse is done by using two pointers, one point at the head and the 
	 * other point at the tail, after switch these two, these two pointers move 
	 * one position towards the middle.
	 */
	public static void rotate_1(int[] nums, int k) {
		if (nums == null || nums.length < 2) {
			return;
		}

		k = k % nums.length;
		reverse(nums, 0, nums.length - k - 1);
		reverse(nums, nums.length - k, nums.length - 1);
		reverse(nums, 0, nums.length - 1);

	}

	private static void reverse(int[] nums, int i, int j) {
		int tmp = 0;
		while (i < j) {
			tmp = nums[i];
			nums[i] = nums[j];
			nums[j] = tmp;
			i++;
			j--;
		}
	}

	public static void rotate_2(int[] nums, int k) {
		if (nums.length <= 1) {
			return;
		}
		//step each time to move
		int step = k % nums.length;
		int[] tmp = new int[step];
		for (int i = 0; i < step; i++) {
			tmp[i] = nums[nums.length - step + i];
		}
		for (int i = nums.length - step - 1; i >= 0; i--) {
			nums[i + step] = nums[i];
		}
		for (int i = 0; i < step; i++) {
			nums[i] = tmp[i];
		}
	}

	public static void rotate(int[] nums, int k) {
		rotate_2(nums, k);
	}

	@Test
	public void test() {
		int[] arr = new int[] { 0, 1, 2, 3, 4, 5, 6, 7 };
		rotate(arr, 3);
		System.out.println(Arrays.toString(arr));
		assertTrue("Test1", Arrays.toString(arr).compareTo("[5, 6, 7, 0, 1, 2, 3, 4]") == 0);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P189_RotateArray.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
