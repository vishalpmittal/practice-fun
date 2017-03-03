package javabrains013;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.annotation.Resource;

public class Circle implements Shape {

    private Point center;

    public Point getCenter() {
        return center;
    }

    /* If name is not specified, there should be a bean in xml with id as "center" */
    @Resource(name = "point3ID")
    public void setCenter(Point center) {
        this.center = center;
    }

    public void draw() {
        System.out.println("Drawing Circle");
        System.out.println("Circle: Point is: " + center.toString());
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

}
