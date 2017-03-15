package javaMisc.oops;

class Parent1 {
    // No specific constructor
    {
        System.out.print("P1B1_");
    }
}

class Parent2 {
    {
        System.out.print("P2B1_");
    }

    public Parent2() {
        System.out.print("P2_");
    }

    {
        System.out.print("P2B2_");
    }
}

class Parent3 {
    {
        System.out.print("P3B1_");
    }

    public Parent3(String x) {
        System.out.print("P3_");
    }

    {
        System.out.print("P3B2_");
    }
}

class Parent4 {
    {
        System.out.print("P4B1_");
    }

    public Parent4() {
        System.out.print("P41_");
    }

    {
        System.out.print("P4B2_");
    }

    public Parent4(int x) {
        this();
        System.out.print("P42_");
    }

    {
        System.out.print("P4B3_");
    }

    public Parent4(String x) {
        this();
        System.out.print("P43_");
    }

    {
        System.out.print("P4B4_");
    }
}

class Child1 extends Parent1 {
    {
        System.out.print("C1B1_");
    }

    public Child1(String x) {
        System.out.print("C1_");
    }

    {
        System.out.print("C1B2_");
    }
}

class Child2 extends Parent2 {
    {
        System.out.print("C2B1_");
    }

    public Child2() {
        System.out.print("C2_");
    }

    {
        System.out.print("C2B2_");
    }
}

class Child3 extends Parent3 {
    {
        System.out.print("C1B1_");
    }
    // Implicit super constructor oops.Parent3() is undefined. Must explicitly invoke another constructor
    // public oops.Child3(String x){ System.out.print("C1_"); }

    public Child3(String x) {
        super(x);
        System.out.print("C1_");
    }

    {
        System.out.print("C1B2_");
    }
}

class Child4 extends Parent4 {
    {
        System.out.print("C4B1_");
    }

    public Child4(String x) {
        super(x);
        System.out.print("C4_");
    }

    {
        System.out.print("C4B2_");
    }
}

public class ConstructorVsInitBlockSample {
    public static void main(String args[]) {
        Child1 c1 = new Child1("c1");               // P1B1_C1B1_C1B2_C1_
        System.out.println();
        Child2 c2 = new Child2();                   // P2B1_P2B2_P2_C2B1_C2B2_C2_
        System.out.println();
        Child3 c3 = new Child3("c3");               // P3B1_P3B2_P3_C1B1_C1B2_C1_
        System.out.println();
        Child4 c4 = new Child4("c4");               // P4B1_P4B2_P4B3_P4B4_P41_P43_C4B1_C4B2_C4_
    }
}
