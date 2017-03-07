package ocpjp.unit1.p1;

public class Sample {

    public int val0 = 1000;
    protected int val1 = 900;
    protected int val2 = 600;
}

class SampleChild extends Sample {
    public void m1() {
        Sample s = new Sample();
        s.val0 = 1000;   // accessing through obj ref

        val0 = 900;   // accessing through inheritence
        val1 = 900;
        // val2 = 900;
    }
}