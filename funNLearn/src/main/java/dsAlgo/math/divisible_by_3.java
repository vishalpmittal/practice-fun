/**
 * Tag: string, math
 * 
 * You are given a string S, consisting of N digits, that represents a number. You 
 * can change at most one digit in the string to any other digit. How many different numbers 
 * divisible by 3 can be obtained in this way?
 * 
 * write a function that, given a string S of length N, returns an integer specifying how many
 * numbers divisible by 3 can be obtained with at most one change of a digit. 
 * 
 * Examples:
 * 1. Input: 23
 * output: 7, (03, 21, 24, 27, 27, 33, 63, 93)
 * 
 * 2. Input: 0081, Output: 11
 * 3. Input: 022, Output: 9 
 * 
 * Write an efficient algorithm for the following assumptions:
 * - N is an integer within the range  [1... 100,000]
 * - string S consists only of digits (0-9)
 */


import java.util.*;

class Solution {
    public static int solution(String S) {
        if (S == null || S.length() == 0){
            return 0;
        }

        try{
            int whole_num = Integer.parseInt(S);
        }catch (NumberFormatException nfe){
            return 0;
        }

        List<Integer> digits = new ArrayList<Integer>();
        int total_sum = 0;
        for (String ch: S.split("")){
            int curr_digit = Integer.parseInt(ch);
            total_sum += curr_digit;
            digits.add(curr_digit);
        }

        int total_divisibles = 0;
        if (total_sum != 0 && total_sum % 3 == 0){
            total_divisibles++;
        }

        for (int x: digits){
            int curr_sum = total_sum - x;

            for (int i = 0; i < 10; i++){

                if (i == x || curr_sum + i == 0){
                    continue;
                }
                else if ((curr_sum + i)%3 == 0){
                    total_divisibles++;
                }
            }
        }
        return total_divisibles;
    }


    public static void main(String args[]){
        assert(Solution.solution("23") == 7);
        assert(Solution.solution("0081") == 11);
        assert(Solution.solution("022") == 9);
        assert(Solution.solution("") == 7);
        assert(Solution.solution("1") == 7);
        assert(Solution.solution("100") == 7);
        assert(Solution.solution("0") == 7);
        assert(Solution.solution("00") == 7);
        assert(Solution.solution("111") == 7);
        assert(Solution.solution("12345678") == 7);
        assert(Solution.solution("badtest") == 7);
        System.out.println("Tests Paased!");
    }
}

