package javaMisc.concurrent.exampleRunnable;

public class ThreadsExample {

    public static void main(String[] args) throws InterruptedException {
        Thread.sleep(4000);
        Thread currentThread = Thread.currentThread();
        System.out.println(currentThread.getName());

        MyThread1 mt1 = new MyThread1();   // new state
        mt1.setName("java.concurrent.MyThread1");
        mt1.start();

        Runnable mt2 = new MyThread2();
        Thread t = new Thread(mt2);      // new state
        t.setName("java.concurrent.MyThread2");
        t.start();

    }
}

class MyThread1 extends Thread {

    public void run() {
        for (int i = 0; i < 5; i++) {
            Thread currentThread = Thread.currentThread();
            System.out.println(currentThread.getName());
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            System.out.println(i);
        }
    }
}

class MyThread2 implements Runnable {

    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            Thread currentThread = Thread.currentThread();
            System.out.println(currentThread.getName());
            System.out.println(i);
        }
    }

}
