/**
 * tag: array
 * 
 * You are given two arrays A and B consisting of N integers each.
 * Index K is named fair if the four sums (A[0] + ... + A[K-1]), (A[K] +... + A[N-1]), 
 * (B[0] + .. + B[K-1]) and (B[K] + ... + B[N-1]) are all equal. 
 * 
 * In other words, K is the index where the two arrays, A and B, can be split 
 * (into two non-empty arrays each) in such a way that the sums of the 
 * resulting arrays elements are equal.
 * 
 * For example, given arrays A = [4, -1, 0, 3] and B = [-2, 5, 0, 3], 
 * index K = 2 is fair. 
 * The sums of the subarrays are all equal: 
 * 4 + (-1) = 3; 0 + 3 = 3; -2 + 5 = 3 and 0 + 3 = 3. 
 * On the other hand, index K = 1 is not fair, 
 * the sums of the subarrays are: 4; (-1) + 0 + 3 = 2; -2 and5+0+3 =8.
 * 
 * given two arrays of integers A and B, returns the number of fair indexes.
 * Examples:
 * 
 * 1. Given A = [4, -1, 0, 3] and B = [-2, 5, 0, 3], your function should return 2. 
 * The fairindexes are 2 and 3. In both cases, the sums of elements of the subarrays 
 * are equal to 3.
 * 
 * 2. Given A = [2, -2, -3, 3] and B = [0, 0, 4, -4], your function should return 1. 
 * The only fair index is 2. 
 * Index 4 is not fair as the subarrays containing indexes from K to N - 1 would be empty.
 * 
 * 3. Given A = [4, -1, 0, 3] and B = [-2, 6, 0, 4], your function should return 0. 
 * There are no fair indexes.
 * 
 * 4. Given A = [3, 2, 6] and B = [4, 1, 6], your function should return 0.
 * 
 * 5. Given A = [1, 4, 2, -2, 5], B = [7, -2, -2, 2, 5], your function should return 2. 
 * The fair indexes are 2 and 4.
 * 
 * Assumptions:
 * -  Nis an integer within the range [2..100,000);
 * -  each element of arrays A, B is an integer within the range [-1,000,000,000..1,000,000,000].
*/

package dsAlgo.list;

import java.util.Arrays;

public class FairArrays {
    public int areFairArrays(int[] A, int[] B) {
        if ((A.length != B.length) || A.length < 1)
            return 0;

        int sumA = A[0];
        for (int a = 1; a < A.length; a++) {
            sumA += A[a];
            A[a] = sumA;
        }

        int sumB = B[0];
        for (int b = 1; b < B.length; b++) {
            sumB += B[b];
            B[b] = sumB;
        }

        int count = 0;
        for (int i = 1; i < A.length; i++) {
            if ((A[i - 1] == B[i - 1]) && (A[i - 1] == sumA - A[i - 1]) && (B[i - 1] == sumB - B[i - 1]))
                count++;
        }

        return count;
    }

    public static void main(String args[]) {
        FairArrays fa = new FairArrays();

        int[][] inputA = { { 4, -1, 0, 3 }, { 2, -2, -3, 3 }, { 4, -1, 0, 3 }, { 3, 2, 6 }, { 1, 4, 2, -2, 5 } };
        int[][] inputB = { { -2, 5, 0, 3 }, { 0, 0, 4, -4 }, { -2, 6, 0, 4 }, { 4, 1, 6 }, { 7, -2, -2, 2, 5 } };
        int[] output = { 2, 1, 0, 0, 2 };

        boolean passed = true;
        for (int i = 0; i < inputA.length; i++) {
            if (fa.areFairArrays(inputA[i], inputB[i]) != output[i]) {
                System.out.printf("Failed test! InputA: %s, InputB: %s, Output: %s\n", Arrays.toString(inputA[i]),
                        Arrays.toString(inputB[i]), output[i]);
                passed = false;
            }
        }
        if (passed)
            System.out.println("Tests Passed!");
    }

}