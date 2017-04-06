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
public class UserDetails_V9 {

    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    @Column(name = "USER_ID")
    private int userId;

    @Column(name = "USER_NAME")
    private String userName;

    /* Hibernate: select next_val as id_val from hibernate_sequence for update
     * Hibernate: update hibernate_sequence set next_val= ? where next_val=?
     * Hibernate: select next_val as id_val from hibernate_sequence for update
     * Hibernate: update hibernate_sequence set next_val= ? where next_val=?
     * Hibernate: select next_val as id_val from hibernate_sequence for update
     * Hibernate: update hibernate_sequence set next_val= ? where next_val=?
     * Hibernate: insert into USER_DETAILS (USER_NAME, USER_ID) values (?, ?)
     * Hibernate: insert into VEHICLE (OWNER_ID, vehicleName, vehicleId) values (?, ?, ?)
     * Hibernate: insert into VEHICLE (OWNER_ID, vehicleName, vehicleId) values (?, ?, ?) */
    @OneToMany(mappedBy = "owner")
    private Collection<Vehicle_V9> vehicles = new ArrayList<Vehicle_V9>();;

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

    public Collection<Vehicle_V9> getVehicles() {
        return vehicles;
    }

    public void setVehicles(Collection<Vehicle_V9> vehicles) {
        this.vehicles = vehicles;
    }

    /* Adding a bidirectional relationship */
    public void addVehicle(Vehicle_V9 vehicle) {
        this.getVehicles().add(vehicle);
        vehicle.setOwner(this);
    }

}
