package javabrains003;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp003 {

    public static void main(String[] args) {
        // ApplicationContext context = new ClassPathXmlApplicationContext("springXMLs/javabrains003.xml");
        // ApplicationContext context = new ClassPathXmlApplicationContext(
        // "springXMLs/javabrains003Alternative.xml");
        ApplicationContext context = new ClassPathXmlApplicationContext(
                "springXMLs/javabrains003Autowire.xml");

        Triangle triangle = (Triangle) context.getBean("triangleid");
        triangle.draw();
    }
}
