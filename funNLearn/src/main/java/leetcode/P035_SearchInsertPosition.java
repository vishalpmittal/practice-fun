package leetcode;

import static org.junit.Assert.assertTrue;

/*
 * Given a sorted array and a target value, return the index if the target is found. 
 * If not, return the index where it would be if it were inserted in order.
 * 
 * You may assume no duplicates in the array.
 * 
 * Here are few examples.
 * [1,3,5,6], 5 → 2
 * [1,3,5,6], 2 → 1
 * [1,3,5,6], 7 → 4
 * [1,3,5,6], 0 → 0
 * */

public class P035_SearchInsertPosition {

    public static int searchInsert(int[] nums, int target) {
        if (nums.length == 0 || target <= nums[0])
            return 0;
        int i = 0;
        for (i = 0; i < nums.length - 1; i++) {
            if (target > nums[i] && target <= nums[i + 1])
                return i + 1;
        }

        return i + 1;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 3, 5, 6 };
        int[] arr1 = { 1 };

        assertTrue("Test1", searchInsert(arr, 5) == 2);
        assertTrue("Test2", searchInsert(arr, 2) == 1);
        assertTrue("Test3", searchInsert(arr, 7) == 4);
        assertTrue("Test4", searchInsert(arr, 0) == 0);
        assertTrue("Test5", searchInsert(arr1, 1) == 0);
        System.out.println("All Tests passed");
    }

}
