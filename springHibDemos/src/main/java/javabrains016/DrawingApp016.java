package javabrains016;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp016 {

    public static void main(String[] args) {
        ApplicationContext context_1 = new ClassPathXmlApplicationContext(
                "springXMLs/javabrains016.xml");
        Shape shape = (Shape) context_1.getBean("circle");
        shape.draw();

        // One of the ways to get message using application context
        // other way is inbuilt in the circle class itself.
        // System.out.println(context_1.getMessage("greetings", null,
        // "Default Greeting", null));
    }
}
