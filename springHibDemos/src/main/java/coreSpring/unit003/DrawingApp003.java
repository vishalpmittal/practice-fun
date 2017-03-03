package coreSpring.unit003;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp003 {

    public static void main(String[] args) {
        // ApplicationContext context = new ClassPathXmlApplicationContext("coreSpring/springXMLs/app003.xml");
        // ApplicationContext context = new ClassPathXmlApplicationContext(
        // "coreSpring/springXMLs/app003Alternative.xml");
        ApplicationContext context = new ClassPathXmlApplicationContext(
                "coreSpring/springXMLs/app003Autowire.xml");

        Triangle triangle = (Triangle) context.getBean("triangleid");
        triangle.draw();
    }
}
