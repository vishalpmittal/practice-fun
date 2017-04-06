package exec;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V90;
import dto.Vehicle_V90;

public class HibernateTest_V90 {

    public static void main(String[] args) {
        UserDetails_V90 user1 = new UserDetails_V90();
        user1.setUserName("User1");

        UserDetails_V90 user2 = new UserDetails_V90();
        user2.setUserName("User2");

        Vehicle_V90 vehicle1 = new Vehicle_V90();
        vehicle1.setVehicleName("User1s car");

        Vehicle_V90 vehicle2 = new Vehicle_V90();
        vehicle1.setVehicleName("User1s Motorcycle");

        user1.addVehicle(vehicle1);
        user1.addVehicle(vehicle2);

        user2.addVehicle(vehicle2);

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();

        session.save(user1);
        session.save(user2);
        session.save(vehicle1);
        session.save(vehicle2);

        session.getTransaction().commit();
        session.close();
        sessionFactory.close();
    }
}
