package dataAccessSpring.jdbcDemo;

import dataAccessSpring.jdbcDemo.dao.JDBCDaoImpl;
import dataAccessSpring.jdbcDemo.model.Circle;

public class JDBCDemo {

    public static void main(String[] args) {
        Circle circle = new JDBCDaoImpl().getCircle(1);
        System.out.println(circle.getName());
    }

}
