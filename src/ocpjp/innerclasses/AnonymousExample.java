package ocpjp.innerclasses;

public class AnonymousExample {

	Animal a = new Animal() {
		public void m1() {
			t1();
			System.out.println("Anonymous");
		}

		public void t1() {
			System.out.println("T1");
		}
	};

	static Thread t = new Thread() {
		public void run() {
		}
	};
	
	static Runnable r = new Runnable() {
		public void run() {
			System.out.println("r");
		}
	};

	public static void main(String[] args) {
		AnonymousExample ax = new AnonymousExample();
		ax.a.m1();
	}

}

class Animal {
	public void m1() {
		System.out.println("From animal");
	}
}

class Horse extends Animal {
	public void m1() {
		System.out.println("From horse");
	}
}