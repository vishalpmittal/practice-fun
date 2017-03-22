package dto;

import java.util.Date;

import javax.persistence.AttributeOverride;
import javax.persistence.AttributeOverrides;
import javax.persistence.Column;
import javax.persistence.Embedded;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

@Entity
@Table(name = "USER_DETAILS")
public class UserDetails_V4 {

    /* Similar to Embedded we have EmbeddedId for embedded objects that are used as primary key */

    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    @Column(name = "USER_ID")
    private int userId;

    @Column(name = "USER_NAME")
    private String userName;

    @Temporal(TemporalType.DATE)
    @Column(name = "JOIN_DATE")
    private Date joinedDate;

    @Embedded
    private Address_V4 homeAddress;

    /* Overrides the column names here */
    @Embedded
    @AttributeOverrides({ @AttributeOverride(name = "street", column = @Column(name = "OFFICE_STREET_NAME")),
            @AttributeOverride(name = "city", column = @Column(name = "OFFICE_CITY_NAME")),
            @AttributeOverride(name = "state", column = @Column(name = "OFFICE_STATE_NAME")),
            @AttributeOverride(name = "pincode", column = @Column(name = "OFFICE_PIN_CODE")) })

    private Address_V4 officeAddress;

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

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Address_V4 getHomeAddress() {
        return homeAddress;
    }

    public void setHomeAddress(Address_V4 homeAddress) {
        this.homeAddress = homeAddress;
    }

    public Address_V4 getOfficeAddress() {
        return officeAddress;
    }

    public void setOfficeAddress(Address_V4 officeAddress) {
        this.officeAddress = officeAddress;
    }

}
