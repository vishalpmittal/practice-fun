package javabrains007;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp007 {

    public static void main(String[] args) {
        // AbstractApplicationContext context = new ClassPathXmlApplicationContext(
        // "springXMLs/javabrains007.xml");
        // context.registerShutdownHook();
        // Triangle triangle = (Triangle) context.getBean("triangleid");
        // triangle.draw();

        AbstractApplicationContext context = new ClassPathXmlApplicationContext(
                "springXMLs/javabrains007Alt.xml");
        context.registerShutdownHook();
        TriangleAlt triangle = (TriangleAlt) context.getBean("triangleid");
        triangle.draw();
    }
}
