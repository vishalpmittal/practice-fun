package javabrains012;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Required;

public class Circle implements Shape {

    private Point center;

    public Point getCenter() {
        return center;
    }

    @Autowired
    @Qualifier("point1ID")
    @Required
    public void setCenter(Point center) {
        this.center = center;
    }

    public void draw() {
        System.out.println("Drawing Circle");
        System.out.println("Circle: Point is: " + center.toString());
    }
}
