package dto;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

@Entity
@Table(name = "VEHICLE")
public class Vehicle_V9 {

    @Id
    @GeneratedValue
    private int vehicleId;
    private String vehicleName;

    /* Adding a bidirectional relationship so that given a vehicle object
     * it's user can be found */

    /* Also unlike V8 we have JoinTable here in vehicle rather than in user
     * in UserDetails_V9 > vehicles, we have specified that the mapping is present here
     * here because each vehicle can have only one owner a new field is added to vehicle table
     * and the user id is added to vehicle table itself. */

    /* Hibernate: select next_val as id_val from hibernate_sequence for update
     * Hibernate: update hibernate_sequence set next_val= ? where next_val=?
     * Hibernate: select next_val as id_val from hibernate_sequence for update
     * Hibernate: update hibernate_sequence set next_val= ? where next_val=?
     * Hibernate: select next_val as id_val from hibernate_sequence for update
     * Hibernate: update hibernate_sequence set next_val= ? where next_val=?
     * Hibernate: insert into USER_DETAILS (USER_NAME, USER_ID) values (?, ?)
     * Hibernate: insert into VEHICLE (OWNER_ID, vehicleName, vehicleId) values (?, ?, ?)
     * Hibernate: insert into VEHICLE (OWNER_ID, vehicleName, vehicleId) values (?, ?, ?) */
    @ManyToOne
    @JoinColumn(name = "OWNER_ID")
    private UserDetails_V9 owner;

    public int getVehicleId() {
        return vehicleId;
    }

    public void setVehicleId(int vehicleId) {
        this.vehicleId = vehicleId;
    }

    public String getVehicleName() {
        return vehicleName;
    }

    public void setVehicleName(String vehicleName) {
        this.vehicleName = vehicleName;
    }

    public UserDetails_V9 getOwner() {
        return owner;
    }

    public void setOwner(UserDetails_V9 owner) {
        this.owner = owner;
    }

}
