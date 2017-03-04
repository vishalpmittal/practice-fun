package vishSpringAOP.unit001.service;

import vishSpringAOP.unit001.model.Circle;
import vishSpringAOP.unit001.model.Triangle;

import vishSpringAOP.unit001.aspect.Loggable;

public class ShapeService {
    private Circle circle;
    private Triangle triangle;

    public Circle getCircle() {
        return circle;
    }

    public void setCircle(Circle circle) {
        this.circle = circle;
    }

    public Triangle getTriangle() {
        return triangle;
    }

    public void setTriangle(Triangle triangle) {
        this.triangle = triangle;
    }

    @Loggable
    public void testMethod() {
        // do nothing
        // this method invocation will call whatever advice is annotated with Loggable
    }
}
