package javaMisc;

/**
 * Java Program which uses varargs feature to accept variable number of
 * arguments. variable arguments are implemented using anonymous array so if
 * another method with exact same signature except array in place of varargs will result
 * in compiler error.
 */
class VarargsExample {

    /* @ return multiplication of all numbers in array
     * - if varargs method accept more than one parameter than varargs arguments
     * must be last parameter.
     * - Call to varargs method should be done using an array
     * eg. Arrays.asList("Red", "White", "Blue"); */
    public int multiply(int... numbers) {
        int result = 1;

        for (int number : numbers) {
            result = result * number;
        }

        return result;
    }
}

/**
 * Java Program which tries to implement variable argument method using
 * method overloading. This started get clumsy once number of parameter exceeds
 * five.
 */
class VarargsExampleArray {

    /* @return multiplication of all numbers in array */
    public int multiply(int[] numbers) {
        int result = 1;

        for (int number : numbers) {
            result = result * number;
        }

        return result;
    }
}

/**
 * Java Program which tries to implement variable argument method using
 * method overloading. This started get clumsy once number of parameter exceeds
 * five.
 */
class VarargsExampleOverloading {

    public int multiply(int a, int b) {
        return a * b;
    }

    public int multiply(int a, int b, int c) {
        return (a * b) * c;
    }

    public int multiply(int a, int b, int c, int d) {
        return (a * b) * (c * d);
    }

}
