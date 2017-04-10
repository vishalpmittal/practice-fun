package dto;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.NamedNativeQuery;
import javax.persistence.NamedQuery;

@Entity(name = "USER_DETAILS")
@NamedQuery(name = "userDetails.byId", query = "from USER_DETAILS where userId = :userId")
@NamedNativeQuery(name = "userDetails.byName", query = "Select * from USER_DETAILS where USER_NAME = :userName", resultClass = UserDetails_V003.class)
public class UserDetails_V003 {
    @Id
    @Column(name = "USER_ID")
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int userId;

    @Column(name = "USER_NAME")
    private String userName;

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    @Override
    public String toString() {
        return "UserDetails_V003 [userId=" + userId + ", userName=" + userName + "]";
    }

}
