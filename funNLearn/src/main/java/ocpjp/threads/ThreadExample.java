package ocpjp.threads;

public class ThreadExample {

    /**
     * @param args
     * @throws InterruptedException
     */
    public static void main(String[] args) throws InterruptedException {
        MT1 mt1 = new MT1();
        MT1 mt2 = new MT1();
        mt1.start();
        mt1 = mt2;
        mt1.join();  // NO EFFECT
        System.out.println("In main");

        // mt2.start();
        /* mt1.join();
         * 
         * mt2.join();
         * for(int i=0;i<5;i++)
         * {
         * System.out.println("C");
         * } */

    }

}

class MT1 extends Thread {
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("A");
        }
    }
}

class MT2 extends Thread {
    public void run() {
        for (int i = 0; i < 5; i++) {
            System.out.println("B");

        }
    }
}