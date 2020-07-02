/**
 * Tag: dp
 * 
 * Say you have an array for which the ith element is the price of a given stock on day i.
 * 
 * If you were only permitted to complete at most one transaction 
 * (ie, buy one and sell one share of the stock), 
 * design an algorithm to find the maximum profit.
 * 
 * Hint: Find the maximum difference between any nth number and (n+m)th number
 */

package dsAlgo.leetcode.P1xx;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result; 
import org.junit.runner.notification.Failure;

public class P121_BestTimeToBuyAndSellStock {
	// Dynamic programming concept
	// keep one variable to keep the min of all integers
	// keep another variable to keep max if profit vs. current integer minus min 
	public static int maxProfit_1(int[] prices) {
		int minPrice = Integer.MAX_VALUE;
		int maxProfit = 0;

		for (int i = 0; i < prices.length; i++) {
			minPrice = Math.min(minPrice, prices[i]);
			maxProfit = Math.max(maxProfit, prices[i] - minPrice);
		}
		return maxProfit;
	}

	// The logic to solve this problem is same as "max subarray problem" 
	// using Kadane's Algorithm.
	// All the straight forward solution should work, but if the interviewer 
	// twists the question slightly by giving the difference array of prices, 
	// Ex: for {1, 7, 4, 11}, if he gives {0, 6, -3, 7}, you might end up being confused.
	
	// Here, the logic is to calculate the difference (maxCur += prices[i] - prices[i-1]) 
	// of the original array, and find a contiguous subarray giving maximum profit. 
	// If the difference falls below 0, reset it to zero.
	public static int maxProfit_2(int[] prices) {
        int maxCur = 0, maxSoFar = 0;
        for(int i = 1; i < prices.length; i++) {
            maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
            maxSoFar = Math.max(maxCur, maxSoFar);
        }
        return maxSoFar;
	}
	
	@Test
	public void test() {
		assertTrue("test1", maxProfit_2(new int[] { 4, 8, 9, 2, 15, 6, 5 }) == 13);
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P121_BestTimeToBuyAndSellStock.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
