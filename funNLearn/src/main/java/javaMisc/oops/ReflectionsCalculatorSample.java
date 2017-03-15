package javaMisc.oops;

import java.lang.reflect.InvocationTargetException;
import java.util.Arrays;

public class ReflectionsCalculatorSample {

    public static void main(String[] args) {
        Class<CalculatorRef> calClassObj = CalculatorRef.class;
        System.out.println("Calculator class methods: ");
        Arrays.asList(calClassObj.getMethods()).forEach(met -> System.out.print(met.getName() + ", "));
        System.out.println("\n \nNumber of methods: " + calClassObj.getMethods().length);

        System.out.println("\nCalculator class Fields: ");
        Arrays.asList(calClassObj.getDeclaredFields()).forEach(fil -> System.out.print(fil.getName() + ", "));
        System.out.println("\n");

        CalculatorRef crObj = null;
        try {
            crObj = calClassObj.getConstructor(String.class).newInstance("just like that");
        } catch (InstantiationException | IllegalAccessException | IllegalArgumentException | InvocationTargetException
                | NoSuchMethodException | SecurityException e) {
            e.printStackTrace();
        }

        System.out.println("");
        try {
            int result = (int) calClassObj.getMethod("add", int.class, int.class, int.class).invoke(crObj, 1, 2, 3);
            System.out.println("Method Invocation result: " + result);
        } catch (IllegalAccessException | IllegalArgumentException | InvocationTargetException | NoSuchMethodException
                | SecurityException e) {
            e.printStackTrace();
        }

        /* Other useful methods:
         * .getName();
         * .getSimpleName();
         * .getModifiers();
         * .getPackage();
         * .getSuperclass();
         * .getInterfaces();
         * .getConstructors();
         * .getMethods();
         * .getFields();
         * .getAnnotations(); */
    }

}

class CalculatorRef {

    public static final double PI = 3.14;
    public int justANumber = Integer.MAX_VALUE;

    public CalculatorRef(String s) {
        System.out.println("Constructor invoked with string: " + s);
    }

    public int add(int a, int b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }

    public int substract(int a, int b) {
        return a - b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }

    public double divide(int a, int b) {
        return a / (double) b;
    }

}