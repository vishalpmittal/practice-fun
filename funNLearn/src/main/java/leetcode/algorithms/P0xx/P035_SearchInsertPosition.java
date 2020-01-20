/**
 * Tag: algo, sort, binary search
 * 
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
 */

package leetcode.algorithms.P0xx;
import static org.junit.Assert.assertTrue;

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

    public static int searchInsert_bs(int[] A, int target) {
        int low = 0, high = A.length-1;
        while(low<=high){
            int mid = (low+high)/2;
            if(A[mid] == target) 
                return mid;
            else if(A[mid] > target) 
                high = mid-1;
            else 
                low = mid+1;
        }
        return low;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 3, 5, 6 };
        int[] arr1 = { 1 };

        assertTrue("Test1", searchInsert_bs(arr, 5) == 2);
        assertTrue("Test2", searchInsert_bs(arr, 2) == 1);
        assertTrue("Test3", searchInsert_bs(arr, 7) == 4);
        assertTrue("Test4", searchInsert_bs(arr, 0) == 0);
        assertTrue("Test5", searchInsert_bs(arr1, 1) == 0);
        System.out.println("All Tests passed");
    }

}
