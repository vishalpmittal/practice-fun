package ocpjp.examples;

import java.util.Comparator;
import java.util.LinkedHashSet;
import java.util.Set;

public class Student {

    String name;
    int rollNum;

    public void setRollNum(int rollNum) {
        this.rollNum = rollNum;
    }

    public Student(String name, int rollNum) {
        super();
        this.name = name;
        this.rollNum = rollNum;
    }

    public int hashcode() {
        return name.length();
    }

    public boolean equals(Object obj) {
        if (obj instanceof Student) {
            Student other = (Student) obj;

            return other.name.equals(this.name) && other.rollNum == this.rollNum;
        } else {
            return false;
        }
    }

    public String toString() {
        return "Name: " + name + ", RollNum: " + rollNum;
    }

    /* @Override
     * public int compareTo(Student o) {
     * return this.rollNum - o.rollNum;
     * /*if(this.rollNum > o.rollNum)
     * {
     * return 1;
     * }
     * else if(this.rollNum < o.rollNum)
     * {
     * return -1;
     * }
     * else
     * {
     * return 0;
     * }
     * } */

}

class StudentRollNumComparator implements Comparator<Student> {

    @Override
    public int compare(Student o1, Student o2) {
        return o1.rollNum - o2.rollNum;
    }

}
