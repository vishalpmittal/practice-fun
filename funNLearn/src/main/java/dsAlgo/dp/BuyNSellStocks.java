
/**
 * Tag: dp
 * 
 * Given a list of stock prices ex - {100,180,260,310,535,700,80, 500, 690, 10},
 * return a list of price at which you would buy and sell to maximize profit ->
 * {80, 690}
 * 
 */

import java.util.*;

class Solution {
    public static List<Integer> bestBuyAndSell(List<Integer> stockPrices) {
        int minPrice = Integer.MAX_VALUE;
        int maxPrice = 0;
        int buy = 0;
        int sell = 0;

        for (int i = 0; i < stockPrices.size(); i++) {

            int currPrice = stockPrices.get(i);
            minPrice = Math.min(minPrice, currPrice);
            maxPrice = Math.max(maxPrice, currPrice);

            if (sell - buy < maxPrice - minPrice) {
                sell = maxPrice;
                buy = minPrice;
                maxPrice = 0;
            }
        }

        return List.of(buy, sell);
    }

    public static void main(String[] args) {
        List<Integer> stockPrices = List.of(100, 180, 260, 310, 535, 700, 80, 500, 690, 10);
        System.out.println(bestBuyAndSell(stockPrices));
    }
}
