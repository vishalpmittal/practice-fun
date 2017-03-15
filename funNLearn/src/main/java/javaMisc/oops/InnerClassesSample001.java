package javaMisc.oops;

public class InnerClassesSample001 {
    public static void main(String[] args) {
        Test t = new Test();
        Test.TestI t1 = t.new TestI();

        Test.TestS t2 = new Test.TestS();
    }
}

class Test {
    int ival = 100;
    static int sval = 200;

    public void m1() {
        ival = 900;
        sval = 1000;
    }

    class TestI {
        public void m2() {
            Test t = Test.this;
            ival = 900;
            sval = 1000;
        }
    }

    static class TestS {
        public void m2() {

            // ival = 900;
            sval = 1000;
        }
    }

    public void s1() {
        class MethodL1 {
            public void r1() {
                ival = 900;
                sval = 1000;

                Test t = Test.this;
            }
        }

        MethodL1 ml1 = new MethodL1();
    }
}
