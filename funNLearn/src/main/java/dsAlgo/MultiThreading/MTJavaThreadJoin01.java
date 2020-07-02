package dsAlgo.MultiThreading;

class MyThreadA extends Thread {
    public void run() {
        for (int i = 0; i < 200; i++)
            System.out.println("A");
    }
}

class MyThreadB implements Runnable {
    public void run() {
        for (int i = 0; i < 200; i++)
            System.out.println("B");
    }
}

public class MTJavaThreadJoin01 {
    public static void main(String[] args) throws InterruptedException {
        Thread currThread = Thread.currentThread();
        String name = currThread.getName();
        System.out.println("Thread name: " + name);

        MyThreadA myThreadA = new MyThreadA(); // NEW
        myThreadA.setName("MyT1");

        MyThreadB myThreadBObj = new MyThreadB();

        Thread t = new Thread(myThreadBObj); // NEW t.setName("MT2");
        t.start();

        myThreadA.start();

        // myThreadA.join();
        // t.join();

        Thread.currentThread().join();
        for (int i = 0; i < 5; i++) {
            System.out.println("C");
        }
    }

}
