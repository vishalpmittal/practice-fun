package javaMisc.oops;

public class ConstructorVsInitBlockSample002 {

    public static void main(String[] args) {
        Test5 t = new Test5();
    }
}

// W Q I1 I2 C
class Test5P {
    Test5P() {
        this("abc");
        System.out.println("S");
    }

    Test5P(String str) {
        super();
        System.out.println("Q");
    }

    {
        System.out.println("W");
    }
}

class Test5 extends Test5P {
    Test5() {
        super("s");
        System.out.println("C");
    }

    {
        System.out.println("I1");
    }

    {
        System.out.println("I2");
    }

}
