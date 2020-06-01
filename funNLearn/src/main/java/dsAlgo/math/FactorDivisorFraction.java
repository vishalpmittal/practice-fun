package dsAlgo.math;

import java.util.ArrayList;

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
