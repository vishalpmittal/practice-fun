package coreSpring.unit001;

import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.FileSystemResource;

public class DrawingApp001 {

    public static void main(String[] args) {
//        Triangle triangle = new Triangle();
        BeanFactory factory = new XmlBeanFactory(new FileSystemResource("src/main/java/coreSpring/springXMLs/app001.xml"));
        Triangle triangle = (Triangle) factory.getBean("triangleid");
        triangle.draw();
        
    }

}
