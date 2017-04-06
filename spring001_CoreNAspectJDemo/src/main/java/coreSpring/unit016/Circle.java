package coreSpring.unit016;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.annotation.Resource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.context.ApplicationEventPublisherAware;
import org.springframework.context.MessageSource;
import org.springframework.stereotype.Component;

/*
 * his component annotation is equivalent to 
 *  <bean id="circleId" class="coreSpring.unit013.Circle">
 *  </bean>
 *  
 *   - Disadvantage
 *  but with this we can not have multiple beans of the same type
 */
@Component
public class Circle implements Shape, ApplicationEventPublisherAware {

    private Point center;
    private ApplicationEventPublisher publisher;

    // the better way of getting messages from properties file
    // have a class param and as there is only one defined in the xml autowire it.
    @Autowired
    private MessageSource messageSource;

    public Point getCenter() {
        return center;
    }

    /* If name is not specified, there should be a bean in xml with id as "center" */
    @Resource(name = "point3ID")
    public void setCenter(Point center) {
        this.center = center;
    }

    public MessageSource getMessageSource() {
        return messageSource;
    }

    public void setMessageSource(MessageSource messageSource) {
        this.messageSource = messageSource;
    }

    public void draw() {

        System.out.println(this.messageSource.getMessage("drawing.circle", null,
                "Default drawing circle msg", null));
        System.out.println(this.messageSource.getMessage("drawing.point",
                new Object[] { center.getX(), center.getY() },
                "Default point msg", null));
        // System.out.println("Circle: Point is: " + center.toString());
        System.out.println(this.messageSource.getMessage("greetings", null,
                "Default Greeting", null));

        DrawEvent de = new DrawEvent(this);
        publisher.publishEvent(de);

    }

    /* called right after construction of the bean */
    @PostConstruct
    public void initializeCircle() {
        System.out.println("Init of circle");
    }

    /* called right before construction of the bean */
    @PreDestroy
    public void destroyCircle() {
        System.out.println("Destroy of circle");
    }

    public void setApplicationEventPublisher(
            ApplicationEventPublisher publisher) {
        this.publisher = publisher;
    }
}
