/**
 * Tag: array 
 *
 * Given an array nums, write a function to move all 0's to the end of 
 * it while maintaining the relative order of the non-zero elements.
 * 
 * For example, given nums = [0, 1, 0, 3, 12], after calling your function, 
 * nums should be [1, 3, 12, 0, 0].
 * 
 * Note:
 * You must do this in-place without making a copy of the array.
 * Minimize the total number of operations. 
 */

package dsAlgo.leetcode.P2xx;

import java.util.Arrays;

public class P283_MoveZeroes {
	public static void moveZeroes(int[] nums) {
		if (nums.length == 0) {
			return;
		}

		//last non zero index
		int lnzi = -1;
		for (int i = 0; i < nums.length; i++) {
			// move all the non zeros to front
			if (nums[i] != 0){				
				nums[lnzi+1] = nums[i];
				lnzi++;
			}
		}
		
		// set remaining positions to zero
		for (int i = lnzi+1; i < nums.length; i++) {
			nums[i] = 0;
		}
		
	}

	public static void main(String[] args) {
//		int[] arr1 = {0, 1, 0, 3, 12};
		int[] arr1 = {1, 2, 0, 0, 3, 12, 0, 0, 2, 2, 3, 0, 0, 0, 0};
		moveZeroes(arr1);
		System.out.println(Arrays.toString(arr1));
	}

}
