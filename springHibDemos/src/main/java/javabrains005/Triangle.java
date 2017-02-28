package javabrains005;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.BeanNameAware;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;

public class Triangle implements ApplicationContextAware, BeanNameAware {
    private Point pointA;
    private Point pointB;
    private Point pointC;
    private ApplicationContext context = null;

    public Triangle() {
    }

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

    /* (non-Javadoc)
     * 
     * @see org.springframework.context.ApplicationContextAware#setApplicationContext(org.springframework.context.
     * ApplicationContext)
     * 
     * Loaded before the beans */
    public void setApplicationContext(ApplicationContext context)
            throws BeansException {
        this.context = context;
        System.out.println("Done setting application context to: \n"
                + context.toString());
    }

    /* (non-Javadoc)
     * 
     * @see org.springframework.beans.factory.BeanNameAware#setBeanName(java.lang.String)
     * This means application is aware of the bean name always and it's loaded before any of the beans */
    public void setBeanName(String beanName) {
        System.out.println("Set bean Name to: " + beanName);
    }
}
