package dsAlgo.math;

import java.util.ArrayList;

/**
 * Created by Vishal on 8/27/2015.
 */
public class FactorDivisorFraction {

    public static ArrayList<Integer> getFactors(int num) {
        ArrayList<Integer> factors = new ArrayList<Integer>();
        for (int i = 1; i <= num / 2; i++) {
            if (num % i == 0) {
                factors.add(i);
            }
        }
        return factors;
    }

    public static void pringFactorSets(int num){

    }

}
