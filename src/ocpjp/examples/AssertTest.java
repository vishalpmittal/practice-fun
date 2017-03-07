package ocpjp.examples;

public class AssertTest {

    /**
     * @param args
     */
    public static void main(String[] args) {

        divide(7, 0);

    }

    public static int divide(int a, int b) {

        assert (b != 0);
        int result = a / b;
        return result;
    }
}