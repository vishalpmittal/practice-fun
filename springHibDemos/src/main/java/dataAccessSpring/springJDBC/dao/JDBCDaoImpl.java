package dataAccessSpring.springJDBC.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.namedparam.MapSqlParameterSource;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.jdbc.core.namedparam.SqlParameterSource;
import org.springframework.stereotype.Component;

import dataAccessSpring.springJDBC.model.Circle;
import dataAccessSpring.springJDBC.model.CircleMapper;
import dataAccessSpring.springJDBC.model.CircleSQLQueries;

@Component
public class JDBCDaoImpl {
    private DataSource dataSource;
    private JdbcTemplate jdbcTemplate = new JdbcTemplate();

    private NamedParameterJdbcTemplate namedParameterJdbcTemplate;

    public Circle getCircle(int circleId) {
        Connection conn = null;
        try {

            conn = dataSource.getConnection();
            PreparedStatement ps = conn
                    .prepareStatement(CircleSQLQueries.selectAllByID);

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

    public DataSource getDataSource() {
        return dataSource;
    }

    @Autowired
    public void setDataSource(DataSource dataSource) {
        this.dataSource = dataSource;
        this.jdbcTemplate.setDataSource(dataSource);
        namedParameterJdbcTemplate = new NamedParameterJdbcTemplate(dataSource);
    }

    public JdbcTemplate getJdbcTemplate() {
        return jdbcTemplate;
    }

    public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public int getCircleCount() {
        int count = jdbcTemplate.queryForObject(CircleSQLQueries.countAll,
                Integer.class);
        return count;
    }

    public String getCircleName(int circleId) {
        return jdbcTemplate.queryForObject(CircleSQLQueries.selectNameByID,
                new Object[] { circleId }, String.class);
    }

    public Circle getCircleForId(int circleId) {
        return jdbcTemplate.queryForObject(CircleSQLQueries.selectAllByID,
                new Object[] { circleId }, new CircleMapper());
    }

    public List<Circle> getAllCircles() {
        return jdbcTemplate.query(CircleSQLQueries.selectAll,
                new CircleMapper());

    }

    public void insertCircle(Circle circle) {
        jdbcTemplate.update(CircleSQLQueries.insertCircle,
                new Object[] { circle.getId(), circle.getName() });
    }

    /* This method is same as the above one. But here we do not have to remember
     * the parameter sequence. We can add the params by key value map and thus can
     * be in any order.
     * 
     * Also the query can have the param ids with : in the front and does not have
     * to only include only ? */
    public void insertCircleNamedParam(Circle circle) {
        String sql = "INSERT INTO CIRCLE (ID, NAME) VALUES (:id, :name)";
        SqlParameterSource namedParams = new MapSqlParameterSource("id",
                circle.getId()).addValue("name", circle.getName());

        namedParameterJdbcTemplate.update(sql, namedParams);
    }

    public void deleteCircle(int circleId) {
        jdbcTemplate.update(CircleSQLQueries.deleteCircleById,
                new Object[] { circleId });
    }

    // this can be called to create a different table even though not related to circle
    public void createTriangleTable() {
        String sql = "CREATE TABLE TRIANGLE (ID INTEGER, NAME VARCHAR(50))";
        jdbcTemplate.execute(sql);
    }
}
