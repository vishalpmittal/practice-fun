package dto;

import javax.persistence.DiscriminatorValue;
import javax.persistence.Entity;

@Entity

/* Instead of mentioning class name as discriminator, it will be FourWheelerDis now */
@DiscriminatorValue("FourWheelerDis")
public class FourWheeler_V92 extends Vehicle_V92 {

    private String SteeringWheel;

    public String getSteeringWheel() {
        return SteeringWheel;
    }

    public void setSteeringWheel(String steeringWheel) {
        SteeringWheel = steeringWheel;
    }

}
