package javabrains007;

public class TriangleAlt {
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

    /* if InitializingBean is implemented that is called before this. */
    public void myInit() {
        System.out.println("My init method called for Triangle");
    }

    /* If DisposableBean is implemented that is called before this */
    public void myDestroy() {
        System.out.println("My destroy method called for Triangle");
    }
}
