package dsAlgo.MultiThreading;

public class MTJavaSimplestDeadlock {
    /* This method request two locks, first String and then Integer */
    public void method1() {
        synchronized (String.class) {
            System.out.println("Aquired lock on String.class object");
            synchronized (Integer.class) {
                System.out.println("Aquired lock on Integer.class object");
            }
        }
    }

    /*
     * This method also requests same two lock but in exactly Opposite order i.e.
     * first Integer and then String. This creates potential deadlock, if one thread
     * holds String lock and other holds Integer lock and they wait for each other,
     * forever.
     */
    public void method2() {
        synchronized (Integer.class) {
            System.out.println("Aquired lock on Integer.class object");
            synchronized (String.class) {
                System.out.println("Aquired lock on String.class object");
            }
        }
    }
}

class DeadLockFixed {
    /**
     * Both method are now requesting lock in same order, first Integer and then
     * String. You could have also done reverse e.g. first String and then
     * Integer, both will solve the problem, as long as both method are requesting
     * lock in consistent order.
     */
    public void method1() {
        synchronized (Integer.class) {
            System.out.println("Aquired lock on Integer.class object");
            synchronized (String.class) {
                System.out.println("Aquired lock on String.class object");
            }
        }
    }

    public void method2() {
        synchronized (Integer.class) {
            System.out.println("Aquired lock on Integer.class object");
            synchronized (String.class) {
                System.out.println("Aquired lock on String.class object");
            }
        }
    }
}
