package exec;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V7;
import dto.Vehicle_V7;

public class HibernateTest_V7 {

    public static void main(String[] args) {
        UserDetails_V7 user1 = new UserDetails_V7();
        user1.setUserName("User1");

        Vehicle_V7 vehicle = new Vehicle_V7();
        vehicle.setVehicleName("User1s car");

        /* One to one mapping setup in the DB
         * 
         * Hibernate: insert into USER_DETAILS (USER_NAME, VEHICLE_ID, USER_ID) values (?, ?, ?)
         * Hibernate: insert into VEHICLE (vehicleName, vehicleId) values (?, ?)
         * Hibernate: update USER_DETAILS set USER_NAME=?, VEHICLE_ID=? where USER_ID=? */
        user1.setVehicle(vehicle);

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();
        session.save(user1);

        session.save(vehicle);
        session.getTransaction().commit();

        session.close();
        sessionFactory.close();
    }
}
