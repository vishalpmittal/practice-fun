package javabrains006;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp006 {

    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext(
                "springXMLs/javabrains006.xml");

        Triangle triangle = (Triangle) context.getBean("triangle1");
        Triangle triangle2 = (Triangle) context.getBean("triangle2");
        triangle.draw();
        triangle2.draw();
    }

}
