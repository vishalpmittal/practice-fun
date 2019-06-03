/**
 * Tag: array, math
 *
 * Given an array of size n, find the majority element. 
 * 
 * The majority element is the element that appears more than ⌊ n/2 ⌋ times.
 * 
 * You may assume that the array is non-empty and the majority element always 
 * exist in the array.
 * 
 */

package leetcode.algorithms.P101_P200;

import java.util.Arrays;

public class P169_MajorityElement {

	public static int majorityElement(int[] nums) {
		Arrays.sort(nums);
		int len = nums.length;
		return nums[len / 2];
	}

	/*
	 * Linear Time Majority Vote Algorithm
	 * Boyer-Moore Majority Vote Algorithm
	 * http://www.cs.utexas.edu/~moore/best-ideas/mjrty/index.html
	 * 
	 * http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html
	 * 
	 * This only works if both the assumptions are true
	 */
	public static int majorityElement_1(int[] nums) {
		int major = nums[0], count = 1;
		for (int i = 1; i < nums.length; i++) {
			if (count == 0) {
				count++;
				major = nums[i];
			} else if (major == nums[i]) {
				count++;
			} else
				count--;
		}
		return major;
	}

	public static void main(String[] args) {

	}

}
