package exec;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.FourWheeler_V93;
import dto.TwoWheeler_V93;
import dto.Vehicle_V93;

public class HibernateTest_V93 {

    public static void main(String[] args) {

        Vehicle_V93 vehicle1 = new Vehicle_V93();
        vehicle1.setVehicleName("vehicle1");

        TwoWheeler_V93 bike = new TwoWheeler_V93();
        bike.setVehicleName("HD IRON Sportster 883");
        bike.setSteeringHandle("HD Lowrider handles");

        FourWheeler_V93 car = new FourWheeler_V93();
        car.setVehicleName("Honda Accord EXL");
        car.setSteeringWheel("Honda Accord Emotion Steering Wheel");

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();

        session.save(vehicle1);
        session.save(car);
        session.save(bike);

        session.getTransaction().commit();
        session.close();
        sessionFactory.close();
    }
}
