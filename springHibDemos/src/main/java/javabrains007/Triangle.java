package javabrains007;

import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;

public class Triangle implements InitializingBean, DisposableBean {
    private Point pointA;
    private Point pointB;
    private Point pointC;

    public Point getPointA() {
        return pointA;
    }

    public void setPointA(Point pointA) {
        this.pointA = pointA;
    }

    public Point getPointB() {
        return pointB;
    }

    public void setPointB(Point pointB) {
        this.pointB = pointB;
    }

    public Point getPointC() {
        return pointC;
    }

    public void setPointC(Point pointC) {
        this.pointC = pointC;
    }

    public void draw() {
        System.out.println("Triangle [pointA=" + pointA + ", pointB=" + pointB
                + ", pointC=" + pointC + "]");
    }

    // called when the bean is initialized
    public void afterPropertiesSet() throws Exception {
        System.out
                .println("Initializing beans init method called for Triangle");
    }

    // called when the bean is destroyed
    public void destroy() throws Exception {
        System.out
        .println("DisposableBean destroy method called for Triangle");
    }
}
