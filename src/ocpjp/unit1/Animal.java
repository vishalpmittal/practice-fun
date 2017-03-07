package ocpjp.unit1;

public class Animal {

    public Animal(String str) {
        System.out.println("Animal");
    }

    public static void main(String[] args) {
        // Horse h = new Horse("abc");
    }

    public void m1() {
        m2();
    }

    public void m2() {
        m1();
    }
}

/* Example of recursive calls in constructors
 * ======================================== */
/* class Horse extends Animal {
 * public Horse(String str) {
 * this(6);
 * System.out.println("Horse");
 * }
 * 
 * public Horse(int val) {
 * this();
 * }
 * 
 * public Horse() {
 * this("abc");
 * }
 * } */