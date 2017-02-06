package leetcode.dependencies;


import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class Template {

    public static boolean problem_1(int n) {
        return false;
    }

    public static boolean problem(int n) {
        return problem_1(n);
    }

    public static void main(String[] args) {
        assertTrue("Test1", problem(94));
        assertFalse("Test2", problem(97));
        System.out.println("All Tests passed");
    }
}
