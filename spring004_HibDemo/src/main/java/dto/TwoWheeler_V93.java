package dto;

import javax.persistence.Entity;

@Entity
public class TwoWheeler_V93 extends Vehicle_V93 {

    private String SteeringHandle;

    public String getSteeringHandle() {
        return SteeringHandle;
    }

    public void setSteeringHandle(String steeringHandle) {
        SteeringHandle = steeringHandle;
    }

}
