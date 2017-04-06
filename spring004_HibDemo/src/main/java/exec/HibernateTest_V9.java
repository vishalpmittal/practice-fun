package exec;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V9;
import dto.Vehicle_V9;

public class HibernateTest_V9 {

    public static void main(String[] args) {
        UserDetails_V9 user1 = new UserDetails_V9();
        user1.setUserName("User1");

        Vehicle_V9 vehicle1 = new Vehicle_V9();
        vehicle1.setVehicleName("User1s car");

        Vehicle_V9 vehicle2 = new Vehicle_V9();
        vehicle1.setVehicleName("User1s Motorcycle");

        /* Adding a bidirectional relationship */
        user1.addVehicle(vehicle1);
        user1.addVehicle(vehicle2);

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
