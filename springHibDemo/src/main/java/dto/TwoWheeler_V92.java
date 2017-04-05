package dto;

import javax.persistence.DiscriminatorValue;
import javax.persistence.Entity;

@Entity

/* Instead of mentioning class name as discriminator, it will be TwoWheelerDis now */
@DiscriminatorValue("TwoWheelerDis")
public class TwoWheeler_V92 extends Vehicle_V92 {

    private String SteeringHandle;

    public String getSteeringHandle() {
        return SteeringHandle;
    }

    public void setSteeringHandle(String steeringHandle) {
        SteeringHandle = steeringHandle;
    }

}
