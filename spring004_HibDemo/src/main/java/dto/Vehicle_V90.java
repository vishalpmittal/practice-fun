package dto;

import java.util.ArrayList;
import java.util.Collection;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.persistence.Table;

@Entity
@Table(name = "VEHICLE")
public class Vehicle_V90 {

    @Id
    @GeneratedValue
    private int vehicleId;
    private String vehicleName;

    /* without mappedBy:
     * creates VEHICLE_USER_DETAILS table to store the mappings */

    /* with mappedBy:
     * now it knows that the mapping is already taken care by vehicles in UserDetails_V90
     * so it does not create an additional table and finds the mapping there.
     * It will not create a VEHICLE_USER_DETAILS table */

    /* Similarly, if (mappedBy ="renters") is added to UserDetails_V90, USER_DETAILS_VEHICLE table will
     * not be created and all the mappings will be take care in the VEHICLE_USER_DETAILS table */
    @ManyToMany(mappedBy = "vehicles")
    private Collection<UserDetails_V90> renters = new ArrayList<UserDetails_V90>();

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

    public Collection<UserDetails_V90> getRenters() {
        return renters;
    }

    public void setRenters(Collection<UserDetails_V90> renters) {
        this.renters = renters;
    }

}
