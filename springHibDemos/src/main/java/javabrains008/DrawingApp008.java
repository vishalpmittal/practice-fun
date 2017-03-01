package javabrains008;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class DrawingApp008 {

    public static void main(String[] args) {
        AbstractApplicationContext context = new ClassPathXmlApplicationContext(
                "springXMLs/javabrains008.xml");
        context.registerShutdownHook();
        
        /*In After Initialization method. Bean name is : point1ID
         * In Before Initialization method. Bean name is : point1ID
         * In After Initialization method. Bean name is : point2ID
         * In Before Initialization method. Bean name is : point2ID
         * In After Initialization method. Bean name is : point3ID
         * In Before Initialization method. Bean name is : point3ID
         * In After Initialization method. Bean name is : triangleid
         * In Before Initialization method. Bean name is : triangleid
         * Triangle [pointA=Point [x=0, y=0], pointB=Point [x=-20, y=0], pointC=Point [x=20, y=0]] */
        Triangle triangle = (Triangle) context.getBean("triangleid");
        triangle.draw();

    }
}
