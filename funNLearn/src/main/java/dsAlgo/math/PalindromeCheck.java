package dsAlgo.math;

public class PalindromeCheck {
    private static int reverse(int number) {
        int reverse = 0;
        while (number != 0) {
            reverse = reverse * 10 + number % 10;
            number = number / 10;
        }
        return reverse;
    }

    private static boolean isPalindrome(int number) {
        if (number == reverse(number)) {
            return true;
        }
        return false;
    }

    public static void main(String arg[]) {
        assert (PalindromeCheck.isPalindrome(12321));
        System.out.println("Tests passed!");
    }
}
