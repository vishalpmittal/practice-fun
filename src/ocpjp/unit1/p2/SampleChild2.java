package ocpjp.unit1.p2;

import ocpjp.unit1.p1.Sample;

public class SampleChild2 extends Sample {
    public void m1() {
        Sample s = new Sample();
        s.val0 = 1000;   // accessing through obj ref

        val0 = 900;   // accessing through inheritence
        val1 = 900;
        val2 = 900;
    }
}
