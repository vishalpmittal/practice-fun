package javaMisc;

public class AutoBoxingUnBoxing {

    public static void changeMe_1(int x) {
        x = 2;
        System.out.println("x: " + x);
    }

    public static void changeMe_2(Integer y) {
        y = new Integer(2);
        System.out.println("y: " + y);
    }

    public static void main(String args[]) {
        Integer a = new Integer(1);
        changeMe_1(a);
        System.out.println("a: " + a);

        a = new Integer(1);
        changeMe_2(a);
        System.out.println("a: " + a);

        int b = 1;
        changeMe_1(b);
        System.out.println("b: " + b);

        b = 1;
        changeMe_2(b);
        System.out.println("b: " + b);

    }

}
