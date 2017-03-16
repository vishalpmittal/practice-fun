package javaMisc.oops;

import java.util.Comparator;
import java.util.HashSet;
import java.util.Set;

public class ComparatorSortingSample {

    public static void main(String[] args) {

        StudentC st1 = new StudentC("A", 3);
        StudentC st2 = new StudentC("C", 1);
        StudentC st3 = new StudentC("D", 2);
        StudentC st4 = new StudentC("B", 4);

        Set<StudentC> studentList = new HashSet<StudentC>();
        studentList.add(st1);
        studentList.add(st2);
        studentList.add(st3);
        studentList.add(st4);

        // Collections.sort(studentList, new StudentRollNumComparator());
        System.out.println(studentList);
    }

}

class StudentC {

    String name;
    int rollNum;

    public void setRollNum(int rollNum) {
        this.rollNum = rollNum;
    }

    public StudentC(String name, int rollNum) {
        super();
        this.name = name;
        this.rollNum = rollNum;
    }

    public int hashcode() {
        return name.length();
    }

    public boolean equals(Object obj) {
        if (obj instanceof StudentC) {
            StudentC other = (StudentC) obj;

            return other.name.equals(this.name) && other.rollNum == this.rollNum;
        } else {
            return false;
        }
    }

    public String toString() {
        return "Name: " + name + ", RollNum: " + rollNum;
    }

    // @Override
    // public int compareTo(Student o) {
    // return this.rollNum - o.rollNum;
    // if (this.rollNum > o.rollNum) {
    // return 1;
    // } else if (this.rollNum < o.rollNum) {
    // return -1;
    // } else {
    // return 0;
    // }
    // }

}

class StudentRollNumComparator implements Comparator<StudentC> {
    @Override
    public int compare(StudentC o1, StudentC o2) {
        return o1.rollNum - o2.rollNum;
    }
}
