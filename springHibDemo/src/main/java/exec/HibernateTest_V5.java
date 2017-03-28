package exec;

import java.util.Date;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V3;
import dto.UserDetails_V5;

public class HibernateTest_V5 {

    public static void main(String[] args) {
        UserDetails_V5 user1 = new UserDetails_V5();
        user1.setUserName("User1");
        user1.setJoinedDate(new Date());

        UserDetails_V5 user2 = new UserDetails_V5();
        user2.setUserName("User2");
        user2.setJoinedDate(new Date());

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();

        session.save(user1);
        session.save(user2);

        // commit the transaction
        session.getTransaction().commit();
        session.close();
        sessionFactory.close();

    }
}
