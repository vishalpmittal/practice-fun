package javabrains005;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp005 {

    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext(
                "springXMLs/javabrains005.xml");
        Triangle triangle = (Triangle) context.getBean("triangleid");
        triangle.draw();

    }

}
