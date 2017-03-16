package javaMisc.oops;

public class InnerClassesSample003 {

    private static int ivar = 20;
    static int svar = 200;

    public static void m1() {

        Thread t = new Thread() {
            public void run() {
                for (int i = 0; i < 5; i++) {
                    System.out.println("A");
                }
            }
        };

        t.start();

    }

    static class ISample {
        public void m2() {
            ivar = 1000;
            svar = 5000;
        }
    }
}

class Tester {
    public static void t1() {
        InnerClassesSample003.ISample is = new InnerClassesSample003.ISample();
    }
}