package exec;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V8;
import dto.Vehicle_V8;

public class HibernateTest_V8 {

    public static void main(String[] args) {
        UserDetails_V8 user1 = new UserDetails_V8();
        user1.setUserName("User1");

        Vehicle_V8 vehicle1 = new Vehicle_V8();
        vehicle1.setVehicleName("User1s car");

        Vehicle_V8 vehicle2 = new Vehicle_V8();
        vehicle1.setVehicleName("User1s Motorcycle");

        /* One to many mapping between the objects
         * Hibernate creates a new table that keeps the mapping between the two */
        user1.getVehicles().add(vehicle1);
        user1.getVehicles().add(vehicle2);

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();

        session.save(user1);
        session.save(vehicle1);
        session.save(vehicle2);

        session.getTransaction().commit();
        session.close();
        sessionFactory.close();
    }
}
