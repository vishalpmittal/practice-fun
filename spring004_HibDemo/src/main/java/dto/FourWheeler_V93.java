package dto;

import javax.persistence.Entity;

@Entity
public class FourWheeler_V93 extends Vehicle_V93 {

    private String SteeringWheel;

    public String getSteeringWheel() {
        return SteeringWheel;
    }

    public void setSteeringWheel(String steeringWheel) {
        SteeringWheel = steeringWheel;
    }

}
