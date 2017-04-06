package exec;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V001;

public class HibernateTest_V001 {

    public static void main(String[] args) {
        UserDetails_V001 user = new UserDetails_V001();
        user.setUserId(3);
        user.setUserName("UserNameWithID3");

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();

        session.save(user);

        session.getTransaction().commit();
        session.close();
        sessionFactory.close();

    }
}
