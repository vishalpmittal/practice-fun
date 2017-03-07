package ocpjp.unit2;

public class Employee {
    public void checkCar(Car c) {
        System.out.println("In Employee");
    }

    public static void main(String[] args) {
        Employee e = new Manager();
        Car c = new BMW();
        e.checkCar(c);
    }

}

class Manager extends Employee {
    public void checkCar(BMW c) {
        System.out.println("In Manager");
    }
}

class Car {

}

class BMW extends Car {

}
