package dto;

import java.util.Date;

import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
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
public class UserDetails_V2 {

    @Id
    @Column(name = "USER_ID")
    private int userId;

    @Column(name = "USER_NAME")
    private String userName;

    /* @Temporal(TemporalType.DATE) : only save the date and not the time
     * 
     * @Temporal(TemporalType.TIME) : only time and not the date
     * 
     * @Temporal(TemporalType.TIMESTAMP) : the entire timestamp */
    @Temporal(TemporalType.DATE)
    private Date joinedDate;
    private String address;

    /* @Lob : its a large object, by default it's clob (character large object)
     * user can also specify blob (byte large object) */
    //@Lob
    private String description;

    /* Hibernate will ignore Transient fields and not save them in the db */
    @Transient
    private String ignoredField;

    /* Hibernate will ignore static fields and not save them in the db */
    private static String dept = "MyDept";

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
