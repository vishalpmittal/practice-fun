package java.concurrent;

public class ThreadsJoinExample {

	/**
	 * @param args
	 * @throws InterruptedException 
	 */
	public static void main(String[] args) throws InterruptedException {
		Thread1 t1 = new Thread1();
		Thread2 t2 = new Thread2();
		t1.start();
		t2.start();
		t1.join(1000);
		t2.join();
		Thread.sleep(1000);
		for (int i = 0; i < 5; i++) {
			System.out.println("B");
		}
	}

}

class Thread1 extends Thread {
	public void run() {
		for (int i = 0; i < 5; i++) {
			System.out.println("A");
		}
	}
}

class Thread2 extends Thread {
	public void run() {
		for (int i = 0; i < 5; i++) {
			System.out.println("C");
		}
	}
}