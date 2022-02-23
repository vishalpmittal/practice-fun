

/**
 * Tag: dp
 * 
 * Maximize the profit from buying and selling the stock
 * 
 * RULES:
 * - Buy up to 1 each day.
 * - Sell any amount of shares.
 * - Sell multiple times.
 * 
 * EXAMPLE: stockPrices = [1, 2, 3]
 * buy 1 @ $1
 * buy 1 @ $2
 * sell 2 @ $3 each
 * 
 */


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class BuyNSellStocksMultiDay {
    public static Integer maxProfit2(List<Integer> prices){
        int max_price = prices.get(prices.size()-1);
        int total_profit = 0;
        int i = prices.size()-2;
        while (i >= 0){
            int curr_price = prices.get(i);
            if (curr_price > max_price){
                max_price = curr_price;
            }
            else{
                total_profit += max_price-curr_price;
            }
            i--;
        }
        return total_profit;       
    }
    

    public static Integer maxProfit(List<Integer> prices){
        int total_profit = 0;
        for (int i = 0; i < prices.size(); i++){
            int curr_price = prices.get(i);
            int max_profit = 0;
            for(int j = i+1; j < prices.size(); j++){
                max_profit = Math.max(max_profit, prices.get(j) - curr_price);
            }
            total_profit += max_profit;
        }
        return total_profit;
    }

    public static void main(String[] args) {
        List<Integer> stockPrices = new ArrayList<Integer>(Arrays.asList(1, 3, 2, 5, 2));
        System.out.println(" " + BuyNSellStocksMultiDay.maxProfit2(stockPrices));
        stockPrices = new ArrayList<Integer>(Arrays.asList(1, 2, 3));
        System.out.println(" " + BuyNSellStocksMultiDay.maxProfit2(stockPrices));

    }
}
