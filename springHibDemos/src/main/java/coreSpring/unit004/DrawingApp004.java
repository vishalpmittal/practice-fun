package coreSpring.unit004;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp004 {

    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext(
                "coreSpring/springXMLs/app004.xml");
        Triangle triangle = (Triangle) context.getBean("triangleid");
        triangle.draw();

    }

}
