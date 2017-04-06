package coreSpring.unit012;

import org.springframework.beans.factory.annotation.Required;

public class Triangle implements Shape {
    private Point pointA;
    private Point pointB;
    private Point pointC;

    public Point getPointA() {
        return pointA;
    }

    @Required
    public void setPointA(Point pointA) {
        this.pointA = pointA;
    }

    public Point getPointB() {
        return pointB;
    }

    @Required
    public void setPointB(Point pointB) {
        this.pointB = pointB;
    }

    public Point getPointC() {
        return pointC;
    }

    @Required
    public void setPointC(Point pointC) {
        this.pointC = pointC;
    }

    public void draw() {
        System.out.println("Drawing Triangle");
        System.out.println("Triangle [pointA=" + pointA + ", pointB=" + pointB
                + ", pointC=" + pointC + "]");
    }
}
