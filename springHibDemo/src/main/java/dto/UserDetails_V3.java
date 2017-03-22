package dto;

import java.util.Date;

import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Lob;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
import javax.persistence.Transient;

/*
 * if "name" is provided with entity, it changes the whole entity name in the environment
 * but "name" with Table only changes it with the db and keeps the entity name as is
 */
@Entity
@Table(name = "USER_DETAILS")
public class UserDetails_V3 {

    /* this make hibernate automatically manage user ids for us
     * strategy = GenerationType.IDENTITY : use identity columns in MySQL, SQLServer for unique primary keys
     * strategy = GenerationType.SEQUENCE : use sequence way to come up with new keys, this is default in postgres
     * strategy = GenerationType.TABLE : hibernate will create a separate table to come up with keys
     * strategy = GenerationType.AUTO: will identify the type of DB and take care of it */
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    @Column(name = "USER_ID")
    private int userId;

    @Column(name = "USER_NAME")
    private String userName;

    @Temporal(TemporalType.DATE)
    @Column(name = "JOIN_DATE")
    private Date joinedDate;

    private String address;
    private String description;

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

    public Date getJoinedDate() {
        return joinedDate;
    }

    public void setJoinedDate(Date joinedDate) {
        this.joinedDate = joinedDate;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

}
