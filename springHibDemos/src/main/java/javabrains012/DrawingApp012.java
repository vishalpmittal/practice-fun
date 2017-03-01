package javabrains012;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp012 {

    public static void main(String[] args) {
        ApplicationContext context_1 = new ClassPathXmlApplicationContext(
                "springXMLs/javabrains012_1.xml");
        Shape shape = (Shape) context_1.getBean("circleId");
        shape.draw();
        
        ApplicationContext context_2 = new ClassPathXmlApplicationContext(
                "springXMLs/javabrains012_2.xml");
        shape = (Shape) context_2.getBean("circleId");
        shape.draw();
        
        ApplicationContext context_3 = new ClassPathXmlApplicationContext(
                "springXMLs/javabrains012_3.xml");
        shape = (Shape) context_3.getBean("circleId");
        shape.draw();
    }

}
