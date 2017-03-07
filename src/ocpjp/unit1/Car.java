package ocpjp.unit1;

public abstract class Car {

    public abstract double getTotalSurfaceArea();

    public void m1() {
        String str;
        System.out.println("Car");
    }

    public static void main(String[] args) {
        final double pi;

        final Student st = new Student();   // 1000x
        // st = new Student(); //2000x
        st.name = "xyz";
        // st = null;
        // code using pi

        pi = 0.8;

        // pi = 0.7;
    }
}

class BMW extends Car {
    public double getTotalSurfaceArea() {
        // do calculations
        return 800;
    }
}
