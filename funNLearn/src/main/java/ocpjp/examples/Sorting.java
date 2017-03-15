package ocpjp.examples;

import java.util.HashSet;
import java.util.Set;

public class Sorting {

    public static void main(String[] args) {

        Student st1 = new Student("A", 3);
        Student st2 = new Student("C", 1);
        Student st3 = new Student("D", 2);
        Student st4 = new Student("B", 4);

        Set<Student> studentList = new HashSet<Student>();
        studentList.add(st1);
        studentList.add(st2);
        studentList.add(st3);
        studentList.add(st4);

        // Collections.sort(studentList, new StudentRollNumComparator());

        System.out.println(studentList);
    }

}
