package dto;

import java.util.ArrayList;
import java.util.Collection;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.OneToMany;
import javax.persistence.Table;

@Entity
@Table(name = "USER_DETAILS")
public class UserDetails_V8 {

    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    @Column(name = "USER_ID")
    private int userId;

    @Column(name = "USER_NAME")
    private String userName;

    /* One to many mapping between the objects */
    /* Hibernate: select next_val as id_val from hibernate_sequence for update
     * Hibernate: update hibernate_sequence set next_val= ? where next_val=?
     * Hibernate: select next_val as id_val from hibernate_sequence for update
     * Hibernate: update hibernate_sequence set next_val= ? where next_val=?
     * Hibernate: select next_val as id_val from hibernate_sequence for update
     * Hibernate: update hibernate_sequence set next_val= ? where next_val=?
     * Hibernate: insert into USER_DETAILS (USER_NAME, USER_ID) values (?, ?)
     * Hibernate: insert into VEHICLE (vehicleName, vehicleId) values (?, ?)
     * Hibernate: insert into VEHICLE (vehicleName, vehicleId) values (?, ?)
     * Hibernate: insert into USER_VEHICLE (UV_USER_ID, UV_VEHICLE_ID) values (?, ?)
     * Hibernate: insert into USER_VEHICLE (UV_USER_ID, UV_VEHICLE_ID) values (?, ?) */
    @OneToMany
    @JoinTable(name = "USER_VEHICLE", joinColumns = @JoinColumn(name = "UV_USER_ID"), inverseJoinColumns = @JoinColumn(name = "UV_VEHICLE_ID"))
    private Collection<Vehicle_V8> vehicles = new ArrayList<Vehicle_V8>();;

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

    public Collection<Vehicle_V8> getVehicles() {
        return vehicles;
    }

    public void setVehicles(Collection<Vehicle_V8> vehicles) {
        this.vehicles = vehicles;
    }

}
