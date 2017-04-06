package dataAccessSpring.springJDBC.model;

public class CircleSQLQueries {

    public static String selectAll = "SELECT * FROM CIRCLE";
    public static String selectAllByID = "SELECT * FROM circle where id = ?";
    public static String selectNameByID = "SELECT NAME FROM CIRCLE WHERE ID = ?";
    public static String countAll = "SELECT COUNT(*) FROM CIRCLE";

    public static String insertCircle = "INSERT INTO CIRCLE (ID, NAME) VALUES (?, ?)";

    public static String deleteCircleById = "DELETE FROM CIRCLE WHERE ID = ?";
}
