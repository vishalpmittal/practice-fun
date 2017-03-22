package exec;

import java.util.Date;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V2;

public class HibernateTest_V2 {

    public static void main(String[] args) {
        UserDetails_V2 user = new UserDetails_V2();
        user.setUserId(2);
        user.setUserName("UserNameV2_2");
        user.setAddress("UserNameV2_2 Address");
        user.setJoinedDate(new Date());
        user.setDescription("UserNameV2_2 description");

        // session factory : one per application
        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();

        // get a session from the sessionFactory object
        Session session = sessionFactory.openSession();

        // begin a transaction on that session object
        session.beginTransaction();

        // save the user object
        session.save(user);

        // commit the transaction
        session.getTransaction().commit();
        session.close();

        user = null;

        session = sessionFactory.openSession();
        session.beginTransaction();
        user = (UserDetails_V2) session.get(UserDetails_V2.class, 2);
        System.out.println("User name retrieved is: " + user.getUserName());

        session.close();
        sessionFactory.close();

    }
}
