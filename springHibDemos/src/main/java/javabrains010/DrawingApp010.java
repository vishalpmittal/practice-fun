package javabrains010;

import javax.naming.Context;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp010 {

    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext(
                "springXMLs/javabrains010.xml");

//        Triangle triangle = (Triangle) context.getBean("triangleId");
//        triangle.draw();
//        
//        Circle circle = (Circle) context.getBean("circleId");
//        circle.draw();
        
        
        Shape shape = (Shape) context.getBean("circleId");
        shape.draw();
        shape = (Shape) context.getBean("triangleId");
        shape.draw();
    }

}
