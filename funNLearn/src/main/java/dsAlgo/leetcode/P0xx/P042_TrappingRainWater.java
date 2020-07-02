/**
 * tag: list, dp, rain water
 * 
 * You are given an array with heights of the buildings. 
 * your job is to design an algorithm to calculate total
 * rainfall accumulated on top of those buildings.
 * 
 * eg: {120, 180, 160, 200, 140, 100, 180, 160, 120, 180}
 * answer: 220
 * 
 */

package dsAlgo.leetcode.P0xx;

public class P042_TrappingRainWater {

    public static int waterTrapped(int[] buildingHeights) {
        /**
         * - keep four pointers left, right, leftmax, rightmax 
         * - if the rightmax is less
         * than leftmax, then we have a big pit trap, or the rightmax has reach left max
         * as well. 
         * - if leftMax is still greater, keep adding the difference of leftmax
         * and left to the total count 
         * - as anypoint in time if we have a bigger
         * leftmax, replacing it will keep the previous count and the new count can be added
         */
        int left = 0;
        int right = buildingHeights.length - 1;

        int leftMax = left;
        int rightMax = right;
        int total = 0;

        while (left < right) {
            if (buildingHeights[left] > buildingHeights[leftMax])
                leftMax = left;
            if (buildingHeights[right] > buildingHeights[rightMax])
                rightMax = right;
            if (buildingHeights[leftMax] > buildingHeights[rightMax]) {
                total += buildingHeights[rightMax] - buildingHeights[right];
                right--;
            } else {
                total += buildingHeights[leftMax] - buildingHeights[left];
                left++;
            }
        }
        return total;
    }

    public static void main(String args[]) throws Exception {
        int[] bh = new int[] { 120, 180, 160, 200, 140, 100, 180, 160, 120, 180 };
        System.out.println(P042_TrappingRainWater.waterTrapped(bh));
    }
}
