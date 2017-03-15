package javaMisc.oops;

import static java.lang.Integer.*;
import static java.lang.Long.*;

public class StaticImportSample {

    /**
     * @param args
     */
    public static void main(String[] args) {
        System.out.println(Integer.MAX_VALUE);

        System.out.println(parseInt("984794"));

    }

}

class Student1 {
    private String name;
    private int rollNum;

    public Student1(String name, int rollNum) {
        super();
        this.name = name;
        this.rollNum = rollNum;
    }

    public String getName() {
        return name;
    }

    public int getRollNum() {
        return rollNum;
    }

}