package javaMisc.concurrent;

public class ConcurrentAccountWithdrawSample {

    public static void main(String[] args) {
        Account acc = new Account();
        Withdrawer w1 = new Withdrawer();
        w1.acc = acc;
        Withdrawer w2 = new Withdrawer();
        w2.acc = acc;
        w1.start();
        w2.start();

        Account.test1(8);
    }
}

class Account {
    int balance = 390;

    static Object obj = new Object();

    public void withdraw(int amount) {
        synchronized (this) {
            int diff = balance - amount;
            if (diff > 0) {
                balance -= amount;
            }
        }
    }

    public static synchronized void test(int amount) {
        int diff = 89;
    }

    public static void test1(int amount) {
        // Class cs = Account.class;
        synchronized (obj) {
        }
    }

    public synchronized void withdraw1(int amount) {
        int diff = balance - amount;
        if (diff > 0) {
            balance -= amount;
        }
    }
}

class Withdrawer extends Thread {
    Account acc;

    public void run() {
        for (int i = 0; i < 5; i++) {
            acc.withdraw(100);
        }
    }
}