package dto;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;
import javax.persistence.Table;

@Entity
@Table(name = "USER_DETAILS")
public class UserDetails_V7 {

    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    @Column(name = "USER_ID")
    private int userId;

    @Column(name = "USER_NAME")
    private String userName;

    /* As the name suggests this is OneToOne mapping.
     * One UserDetails_V7 object will have one to one mapping with Vehicle_V7 object */
    @OneToOne
    @JoinColumn(name = "VEHICLE_ID")
    private Vehicle_V7 vehicle;

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

    public Vehicle_V7 getVehicle() {
        return vehicle;
    }

    public void setVehicle(Vehicle_V7 vehicle) {
        this.vehicle = vehicle;
    }

}
