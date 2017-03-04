package vishSpringAOP.unit001;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import vishSpringAOP.unit001.service.ShapeService;

public class AopMain {

    public static void main(String[] args) {
        ApplicationContext ctx = new ClassPathXmlApplicationContext(
                "vishSpringAOP/springAopXMLs/app001.xml");

        ShapeService shapeService = ctx.getBean("shapeService",
                ShapeService.class);
        System.out.println(shapeService.getCircle().getName());
        System.out.println("----------------------");
        System.out.println(shapeService.getTriangle().getName());

    }

}
