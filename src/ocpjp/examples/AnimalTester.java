package ocpjp.examples;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class AnimalTester {

    static List<Integer> list = new ArrayList<Integer>();

    static {
        list.add(5);
        list.add(3);
        list.add(1);
        list.add(8);
        list = Collections.unmodifiableList(list);
    }

    /**
     * @param args
     */
    public static void main(String[] args) {
        list.add(100);
    }

    public static void addToDB(List<? extends Employee> employeeList) {
        for (Employee e : employeeList) {
            // Adding e to Database
        }
        // System.out.println(animalList.size());
        // animalList.add(new Animal());
    }

}

class Employee {

}

class Manager extends Employee {

}

class Director extends Employee {

}