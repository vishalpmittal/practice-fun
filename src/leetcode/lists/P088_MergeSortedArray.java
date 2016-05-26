/*
 * Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
 * 
 * Note:
 * You may assume that nums1 has enough space (size that is greater or equal to m + n) 
 * to hold additional elements from nums2. The number of elements initialized in 
 * nums1 and nums2 are m and n respectively.
 */

package leetcode.lists;

import java.util.Arrays;

public class P088_MergeSortedArray {

	// Start comparing from the beginning
	// Compare and keep saving extras in nums2 while keep saving sorted seried in nums1
	// once done copy nums2 to nums 1
	public static void merge(int[] nums1, int m, int[] nums2, int n) {
		int p1 = 0, p2 = 0;
		if (n < 1)
			return;

		while (p1 < m) {
			if (nums1[p1] <= nums2[p2])
				p1++;
			else {
				int tmp = nums1[p1];
				nums1[p1] = nums2[p2];
				nums2[p2] = tmp;
				p1++;

				while (p2 < n - 1 && nums2[p2] > nums2[p2 + 1]) {
					int tmp2 = nums2[p2];
					nums2[p2] = nums2[p2 + 1];
					nums2[p2 + 1] = tmp2;
					p2++;
				}
				p2 = 0;
			}
		}

		while (p2 < n) {
			nums1[p1] = nums2[p2];
			p1++;
			p2++;
		}
	}

	// Back traversing 
	public static void merge_1(int[] nums1, int m, int[] nums2, int n) {
		int i = m - 1;
		int j = n - 1;
		int k = m + n - 1;

		while (i >= 0 && j >= 0) {
			if (nums1[i] > nums2[j])
				nums1[k--] = nums1[i--];
			else
				nums1[k--] = nums2[j--];
		}
		while (j >= 0)
			nums1[k--] = nums2[j--];
	}

	public static void main(String[] args) {
		//int[] arr1 = { 2, 5, 8, 10, 0, 0, 0, 0, 0, 0, 0, 0 };
		//int[] arr2 = { 1, 3, 6, 8, 9, 0, 0, 0, 0 };

		int[] arr1 = { 2, 0 };
		int[] arr2 = { 1 };

		merge(arr1, 1, arr2, 1);
		System.out.println("----------------------------");
		System.out.println(Arrays.toString(arr1));
		System.out.println(Arrays.toString(arr2));
	}
}
