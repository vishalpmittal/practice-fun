package exec;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V91;
import dto.Vehicle_V91;

public class HibernateTest_V91 {

    public static void main(String[] args) {
        UserDetails_V91 user1 = new UserDetails_V91();
        user1.setUserName("User1");

        Vehicle_V91 vehicle1 = new Vehicle_V91();
        vehicle1.setVehicleName("User1s car");

        Vehicle_V91 vehicle2 = new Vehicle_V91();
        vehicle2.setVehicleName("User1s Motorcycle");

        user1.addVehicle(vehicle1);
        user1.addVehicle(vehicle2);

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();

        /* - here we are not saving any vehicle object
         * - also instead of saving user object we are using persist
         * - session.persist is needed for cascading type PERSIST */
        session.persist(user1);

        session.getTransaction().commit();
        session.close();
        sessionFactory.close();
    }
}
