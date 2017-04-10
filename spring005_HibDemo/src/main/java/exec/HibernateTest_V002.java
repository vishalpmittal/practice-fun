package exec;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V002;

public class HibernateTest_V002 {

    public static void main(String[] args) {

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();

        /* Create some users */
        Session session = sessionFactory.openSession();
        session.beginTransaction();
        for (int i = 0; i < 10; i++) {
            UserDetails_V002 user = new UserDetails_V002();
            user.setUserName("user" + i);
            session.save(user);
        }
        session.getTransaction().commit();
        session.close();
        session = null;

        /* read a user object and close the session */
        session = sessionFactory.openSession();
        session.beginTransaction();
        UserDetails_V002 user = (UserDetails_V002) session.get(UserDetails_V002.class, 6);
        session.getTransaction().commit();
        session.close();
        session = null;

        /* Update the user object without reading it
         * coz we have used following in user details, that will do a select before each update
         * 
         * @SelectBeforeUpdate(value = true)
         * 
         * In current versions it might be true by default
         * in some cases if the object is updated before opening session, doing selectBeforeUpdate might reload
         * the object and updates might be lost. Precaution must be while using this. */
        session = sessionFactory.openSession();
        session.beginTransaction();
        user.setUserName("Updated name");
        session.update(user);
        session.getTransaction().commit();
        session.close();

        sessionFactory.close();

    }
}
