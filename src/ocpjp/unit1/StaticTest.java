package ocpjp.unit1;

public class StaticTest {

	public static void main(String[] args) {
		System.out.println("M");
		Test10 t1 = new Test10();
	}
}

class Test10 {
	Test10() {
		super();
		System.out.println("c0");
	}

	{
		System.out.println("I2");
	}

	static {
		System.out.println("H");
	}

	{
		System.out.println("I1");
	}
}

class Test11 extends Test10 {

	static int val = 90;

	static {
		System.out.println("s1");
	}

	{
		System.out.println("T1");
	}

	Test11() {
		super();
		System.out.println("C1");
	}

	{
		System.out.println("T2");
	}
}
