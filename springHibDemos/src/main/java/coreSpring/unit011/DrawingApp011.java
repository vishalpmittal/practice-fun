package coreSpring.unit011;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp011 {

    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext(
                "coreSpring/springXMLs/app011.xml");

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
