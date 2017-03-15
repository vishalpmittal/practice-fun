/**
 * -  Static blocks are called at class loading
 * -  Instance Init blocks are called at class object instantiating
 * -  constructors are then called. 
 * -  Static blocks are executed just once
 * -  Instance Init blocks and constructor are called at every instantiation
 * */

package javaMisc.oops;

class Parent {
    static {
        System.out.print("PSB1_");
    }
    {
        System.out.print("PB1_");
    }

    public Parent() {
        System.out.print("PC1_");
    }

    static {
        System.out.print("PSB2_");
    }
    {
        System.out.print("PB2_");
    }
}

class Child extends Parent {
    static int val = 100;
    static {
        System.out.print("CSB1_");
    }
    {
        System.out.print("CB1_");
    }

    public Child() {
        System.out.print("CC1_");
    }

    static {
        System.out.print("CSB2_");
    }
    {
        System.out.print("CB2_");
    }

    public Child(int x) {
        this();
        System.out.print("CC2_");
    }

    static {
        System.out.print("CSB3_");
    }
    {
        System.out.print("CB3_");
    }

    public Child(String s) {
        this(5);
        System.out.print("CC3_");
    }

    static {
        System.out.print("CSB4_");
    }
    {
        System.out.print("CB4_");
    }
}

public class StaticVsInitBlockVsConstructorSeqSample001 {
    public static void main(String[] args) {
        System.out.println("M1_");             // M1_
        Child c1;                              // prints nothing
        System.out.println("M2_");             // M2_
        Child.val = 101;                         // PSB1_PSB2_CSB1_CSB2_CSB3_CSB4_
        System.out.println("\nM3_");           // M3_
        Child c3 = new Child("vishal");        // PB1_PB2_PC1_CB1_CB2_CB3_CB4_CC1_CC2_CC3_
        System.out.println("\nM4_");           // M4_
        c3 = new Child("mittal");              // PB1_PB2_PC1_CB1_CB2_CB3_CB4_CC1_CC2_CC3_
        System.out.println("\nM5_");           // M5
    }
}
