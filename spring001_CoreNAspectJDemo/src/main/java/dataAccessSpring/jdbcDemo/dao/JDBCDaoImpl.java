package dataAccessSpring.jdbcDemo.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import dataAccessSpring.jdbcDemo.model.Circle;

public class JDBCDaoImpl {

    private static String derby_driver = "org.apache.derby.jdbc.ClientDriver";
    private static String derby_conn_url = "jdbc:derby://localhost:1527/db";
    private static String selectStmt = "SELECT * FROM circle where id = ?";

    public Circle getCircle(int circleId) {
        Connection conn = null;
        try {
            Class.forName(derby_driver).newInstance();

            conn = DriverManager.getConnection(derby_conn_url);

            PreparedStatement ps = conn.prepareStatement(selectStmt);

            ps.setInt(1, circleId);

            Circle circle = null;
            ResultSet rs = ps.executeQuery();

            if (rs.next()) {
                circle = new Circle(circleId, rs.getString("name"));
            }

            rs.close();
            ps.close();

            return circle;
        } catch (Exception e) {
            throw new RuntimeException();
        } finally {
            try {
                conn.close();
            } catch (SQLException e) {
            }
        }
    }

}
