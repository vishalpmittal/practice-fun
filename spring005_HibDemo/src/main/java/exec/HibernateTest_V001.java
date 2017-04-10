package exec;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V001;

public class HibernateTest_V001 {

    public static void main(String[] args) {

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();

        /* Create */
        for (int i = 0; i < 10; i++) {
            UserDetails_V001 user = new UserDetails_V001();
            user.setUserName("user" + i);
            session.save(user);
        }

        /* Read */
        UserDetails_V001 user = (UserDetails_V001) session.get(UserDetails_V001.class, 6);
        System.out.println("Read username: " + user.getUserName());

        /* Update */
        user.setUserName("Updated name");
        session.update(user);
        user = null;
        user = (UserDetails_V001) session.get(UserDetails_V001.class, 6);
        System.out.println("Read username: " + user.getUserName());

        /* delete */
        session.delete(user);
        user = null;
        try {
            user = (UserDetails_V001) session.get(UserDetails_V001.class, 6);
            System.out.println("Read username: " + user.getUserName());
        } catch (NullPointerException e) {
            System.out.println("The user with ID 6 has been deleted");
        }

        session.getTransaction().commit();
        session.close();
        sessionFactory.close();

    }
}
