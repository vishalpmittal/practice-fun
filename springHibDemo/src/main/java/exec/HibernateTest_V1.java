package exec;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V1;

public class HibernateTest_V1 {

    public static void main(String[] args) {
        UserDetails_V1 user = new UserDetails_V1();
        user.setUserId(3);
        user.setUserName("UserNameWithID3");

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
        sessionFactory.close();

    }
}
