package ocpjp.innerclasses;

public class SampleO {

    static int ivar = 100;
    static int svar = 200;

    class TestI {
        int vag = 0;

        public void m2() {
            // ivar = 1000;
            svar = 30000;
        }
    }

    static class TestS {
        int vag = 0;

        public void m2() {
            // ivar = 1000;
            svar = 30000;
        }
    }

    public void m1() {
        ivar = 1000;
        svar = 30000;

        class MethodInner1 {
            public void s1() {
                ivar = 1000;
                svar = 30000;
            }

        }

        MethodInner1 mi1 = new MethodInner1();

    }

    public static void s1() {
        class MethodInner1 {
            public void s1() {
                ivar = 1000;
                svar = 30000;
            }

        }

    }
}

class Tester1 {
    public static void main() {
        /* SampleO s0 = new SampleO();
         * SampleO.TestI si1 = s0.new TestI();
         * SampleO.TestI si2 = s0.new TestI(); */

        SampleO.TestS ts = new SampleO.TestS();

    }
}
