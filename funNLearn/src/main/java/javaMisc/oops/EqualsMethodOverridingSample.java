package javaMisc.oops;

import java.util.ArrayList;
import java.util.List;

class Student4 {
    String name;
    int rollNum;

    public Student4(String name, int rollNum) {
        super();
        this.name = name;
        this.rollNum = rollNum;
    }

    public int hashcode() {
        return 7;
    }

    public boolean equals(Object obj) {
        if (obj instanceof Student4) {
            Student4 otherStudent = (Student4) obj;
            return this.name.equals(otherStudent.name) && this.rollNum == otherStudent.rollNum;
        } else {
            return false;
        }
    }
}

public class EqualsMethodOverridingSample {

    public static void main(String[] args) {
        Student4 st1 = new Student4("a", 1);
        Student4 st2 = new Student4("b", 2);
        Student4 st3 = new Student4("c", 3);
        Student4 st4 = new Student4("d", 4);

        List<Student4> lt = new ArrayList<Student4>();
        lt.add(st1);
        lt.add(st2);
        lt.add(st3);
        lt.add(st4);

        Student4 st5 = new Student4("a", 1);
        System.out.println(lt.contains(st5));
    }
}
