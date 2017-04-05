package exec;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.FourWheeler_V92;
import dto.TwoWheeler_V92;
import dto.Vehicle_V92;

public class HibernateTest_V92 {

    public static void main(String[] args) {

        Vehicle_V92 vehicle1 = new Vehicle_V92();
        vehicle1.setVehicleName("vehicle1");

        TwoWheeler_V92 bike = new TwoWheeler_V92();
        bike.setVehicleName("HD IRON Sportster 883");
        bike.setSteeringHandle("HD Lowrider handles");

        FourWheeler_V92 car = new FourWheeler_V92();
        car.setVehicleName("Honda Accord EXL");
        car.setSteeringWheel("Honda Accord Emotion Steering Wheel");

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();

        /* Hibernate: create table VEHICLE (DTYPE varchar(31) not null, vehicleId integer not null, vehicleName
         * varchar(255), SteeringHandle varchar(255), SteeringWheel varchar(255), primary key (vehicleId))
         * 
         * Hibernate: insert into VEHICLE (vehicleName, DTYPE, vehicleId) values (?, 'Vehicle_V92', ?)
         * 
         * Hibernate: insert into VEHICLE (vehicleName, SteeringWheel, DTYPE, vehicleId) values (?, ?,
         * 'FourWheeler_V92', ?)
         * 
         * Hibernate: insert into VEHICLE (vehicleName, SteeringHandle, DTYPE, vehicleId) values (?, ?,
         * 'TwoWheeler_V92', ?)
         * 
         * DTYPE is the discriminator type which is the type of object */
        session.save(vehicle1);
        session.save(car);
        session.save(bike);

        session.getTransaction().commit();
        session.close();
        sessionFactory.close();
    }
}
