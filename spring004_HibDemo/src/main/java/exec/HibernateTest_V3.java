package exec;

import java.util.Date;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V2;
import dto.UserDetails_V3;

public class HibernateTest_V3 {

    public static void main(String[] args) {
        UserDetails_V3 user1 = new UserDetails_V3();
        user1.setUserName("User1");
        user1.setAddress("User1 Address");
        user1.setJoinedDate(new Date());
        user1.setDescription("User1 description");

        UserDetails_V3 user2 = new UserDetails_V3();
        user2.setUserName("User2");
        user2.setAddress("user2 Address");
        user2.setJoinedDate(new Date());
        user2.setDescription("user2 description");

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();

        // Even though we are not providing ids Hibernate will auto generate it
        session.save(user1);
        session.save(user2);

        // commit the transaction
        session.getTransaction().commit();
        session.close();
        sessionFactory.close();

    }
}
