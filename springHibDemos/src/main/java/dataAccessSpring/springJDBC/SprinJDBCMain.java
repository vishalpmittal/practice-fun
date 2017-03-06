package dataAccessSpring.springJDBC;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import dataAccessSpring.springJDBC.dao.JDBCDaoImpl;
import dataAccessSpring.springJDBC.model.Circle;

public class SprinJDBCMain {

    public static void main(String[] args) {
        ApplicationContext ctx = new ClassPathXmlApplicationContext(
                "dataAccessSpring/springJDBC/app.xml");
        JDBCDaoImpl dao = ctx.getBean("JDBCDaoImpl", JDBCDaoImpl.class);

        Circle circle = dao.getCircle(1);
        System.out.println("Using JDBC Conn, circle name: " + circle.getName());

        System.out
                .println("Using jdbc template, count: " + dao.getCircleCount());
        System.out.println(
                "Using jdbc template, Circle Name: " + dao.getCircleName(1));

        System.out.println("Using jdbc template and circle mapper, Circle: "
                + dao.getCircleForId(1));

        System.out.println(
                "Using jdbc template and circle mapper, list of all circles: "
                        + dao.getAllCircles());

        dao.insertCircle(new Circle(2, "Second Circle"));
        System.out.println(
                "Using jdbc template and circle mapper, list of all circles: "
                        + dao.getAllCircles());

        dao.insertCircle(new Circle(3, "Third Circle"));
        System.out.println(
                "Using jdbc template and circle mapper, list of all circles: "
                        + dao.getAllCircles());

        dao.deleteCircle(2);
        dao.deleteCircle(3);
        System.out.println(
                "Using jdbc template and circle mapper, list of all circles: "
                        + dao.getAllCircles());
    }

}
