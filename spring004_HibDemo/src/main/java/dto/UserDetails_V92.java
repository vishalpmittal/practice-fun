package dto;

import java.util.ArrayList;
import java.util.Collection;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

@Entity
@Table(name = "USER_DETAILS")
public class UserDetails_V92 {

    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    @Column(name = "USER_ID")
    private int userId;

    @Column(name = "USER_NAME")
    private String userName;

    /* cascade the vehicle object while saving. No explicit vehicle object saving is needed now. */
    @OneToMany(cascade = CascadeType.PERSIST)
    private Collection<Vehicle_V92> vehicles = new ArrayList<Vehicle_V92>();

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

    public Collection<Vehicle_V92> getVehicles() {
        return vehicles;
    }

    public void setVehicles(Collection<Vehicle_V92> vehicles) {
        this.vehicles = vehicles;
    }

    public void addVehicle(Vehicle_V92 vehicle) {
        this.getVehicles().add(vehicle);
    }

}
