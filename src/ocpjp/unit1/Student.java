package ocpjp.unit1;

public class Student {

    public String name = "John"; // Instance variable -> Object reference

    public int rollNum = 50; // Instance variable -> primitive data type

    public static int sval = 1000; // static variable -> primitive data type

    public static String sStr = "xyz"; // static variable -> object reference

    public void m1() // instance method
    {
        Student.sval = 3000;
        System.out.println("M1");
    }

    public static void s1() // static method
    {
        System.out.println("S1");
    }

    public static void main(String[] args) {
        int val = 900; // local variable -> primitive data type
        String str = "abc"; // local variable -> Object reference

        Student st = new Student(); // Object creation
        Student st1 = new Student();
        System.out.println(st.name); // Accessing instance members

        Student.s1(); // Accessing static members
        Student.sval = 5000;
        Student.sStr = "123";
        // TODO Auto-generated method stub
    }

}
