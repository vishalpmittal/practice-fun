package javaMisc.concurrent;

public class BasicThreadUsageSample {

    /**
     * @param args
     * @throws InterruptedException
     */
    public static void main(String[] args) throws InterruptedException {
        String name = Thread.currentThread().getName();
        System.out.println("In main method, thread name: " + name);

        MyThread1 mt1 = new MyThread1(); // NEW STATE
        mt1.setName("MyThread1");

        mt1.start();

        MyThread2 mt2 = new MyThread2();

        Thread t = new Thread(mt2);
        t.setName("MyThread2");
        t.start();
    }
}

class MyThread1 extends Thread {

    public void run() {
        for (int i = 0; i < 5; i++) {
            Thread currentThread = Thread.currentThread();
            String currentThreadName = currentThread.getName(); // main
            String name = getName(); // MyThread1

            Thread.yield();
            System.out.println(System.currentTimeMillis());
            System.out.println("Count : " + i + " , Name: " + name);
        }
    }
}

class MyThread2 implements Runnable {

    public void run() {
        for (int i = 0; i < 5; i++) {
            Thread currentThread = Thread.currentThread();
            String currentThreadName = currentThread.getName(); // main
            System.out.println("Count : " + i + " , Name: " + currentThreadName);
        }
    }
}
