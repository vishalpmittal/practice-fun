package dataAccessSpring.springJDBC.model;

import java.sql.ResultSet;
import java.sql.SQLException;

import org.springframework.jdbc.core.RowMapper;

public final class CircleMapper implements RowMapper<Circle> {

    public Circle mapRow(ResultSet rs, int rowNum) throws SQLException {
        Circle circle = new Circle();
        circle.setId(rs.getInt("ID"));
        circle.setName(rs.getString("NAME"));
        return circle;
    }
}
