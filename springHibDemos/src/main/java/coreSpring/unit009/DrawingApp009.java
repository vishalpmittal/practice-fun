package coreSpring.unit009;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp009 {

    public static void main(String[] args) {
        AbstractApplicationContext context = new ClassPathXmlApplicationContext(
                "coreSpring/springXMLs/app009.xml");
        context.registerShutdownHook();
        
        Triangle triangle = (Triangle) context.getBean("triangleid");
        triangle.draw();

    }
}
