package dto;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;

/*
 * With name property for Entity annotation, hibernate creates the table with the new provided name
 * if no name property present the table name will be the same as class name
 */
@Entity(name = "USER_DETAILS")
public class UserDetails_V1 {

    @Id
    @Column(name = "USER_ID")
    private int userId;

    /* column name in the db will be USER_NAME
     * without the name property column name will be same as field name here */
    @Column(name = "USER_NAME")
    private String userName;

    // @id, @Column annotation can be put on the top of getters as well
    // will behave the same
    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    // @Column annotation can be put on the top of getters as well
    // will behave the same
    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

}
