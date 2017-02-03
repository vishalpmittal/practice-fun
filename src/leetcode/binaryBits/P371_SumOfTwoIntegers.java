package leetcode.binaryBits;

/**
 * Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -
 * 
 * Example:
 * Given a = 1 and b = 2, return 3.
 * 
 * =====================================================================
 * "&" AND operation, for example, 2 (0010) & 7 (0111) => 2 (0010)
 * 
 * "^" XOR operation, for example, 2 (0010) ^ 7 (0111) => 5 (0101)
 * 
 * "~" NOT operation, for example, ~2(0010) => -3 (1101) what??? 
 * Don't get frustrated here. It's called two's complement.
 * 
 * 1111 is -1, in two's complement
 * 
 * 1110 is -2, which is ~2 + 1, ~0010 => 1101, 1101 + 1 = 1110 => 2
 * 
 * 1101 is -3, which is ~3 + 1
 * so if you want to get a negative number, you can simply do ~x + 1
 */

import static org.junit.Assert.assertTrue;

public class P371_SumOfTwoIntegers {

    /*
     * we have a = 1, b = 3,
     * In bit representation, a = 0001, b = 0011,
     * First, we can use "and"("&") operation between a and b to find a carry.
     * carry = a & b, then carry = 0001
     * Second, we can use "xor" ("^") operation between a and b to find the different bit, 
     * and assign it to a,
     * 
     * Then, we shift carry one position left and assign it to b, b = 0010.
     * Iterate until there is no carry (or b == 0)
     * 
     * |---------------------------------------------------|
     * |               |   a = 1   |   b = 3   |   carry   |
     * |---------------|-----------|-----------|-----------|
     * |               |   0001    |    0011   |     -     |
     * |---------------|-----------|-----------|-----------|
     * |carry = a & b  |           |           |   0001    |
     * |a = a ^ b      |   0010    |           |           |
     * |b = carry << 1 |           |  0010     |           |
     * |---------------|-----------|-----------|-----------|
     * |carry = a & b  |           |           |   0010    |
     * |a = a ^ b      |   0000    |           |           |
     * |b = carry << 1 |           |  0100     |           |
     * |---------------|-----------|-----------|-----------|
     * |carry = a & b  |           |           |   0000    |
     * |a = a ^ b      |   0100    |           |           |
     * |b = carry << 1 |           |   0000    |           |
     * |---------------|-----------|-----------|-----------|
     */
    public static int getSum(int a, int b) {
        if (a == 0) return b;
        if (b == 0) return a;

        while (b != 0) {
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        
        return a;
    }

    // Iterative
    public static int getSubtract(int a, int b) {
        while (b != 0) {
            int borrow = (~a) & b;
            a = a ^ b;
            b = borrow << 1;
        }
        
        return a;
    }

    // Recursive
    public static int getSum_1(int a, int b) {
        return (b == 0) ? a : getSum(a ^ b, (a & b) << 1);
    }

    // Recursive
    public static int getSubtract_2(int a, int b) {
        return (b == 0) ? a : getSubtract(a ^ b, (~a & b) << 1);
    }

    // Get negative number
    public int negate(int x) {
        return ~x + 1;
    }

    public static void main(String[] args) {
        assertTrue("Test1", 4 == getSum(1, 3));
        System.out.println("All Tests passed");
    }
}
