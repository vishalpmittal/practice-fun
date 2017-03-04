package vishSpringAOP.unit002;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import vishSpringAOP.unit002.service.ShapeService;

public class AopMain {

    public static void main(String[] args) {
        ApplicationContext ctx = new ClassPathXmlApplicationContext(
                "vishSpringAOP/springAopXMLs/app002.xml");

        ShapeService shapeService = ctx.getBean("shapeService",
                ShapeService.class);
        shapeService.getCircle();

    }
}
