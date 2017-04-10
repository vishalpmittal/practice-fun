package exec;

import java.util.List;

import javax.persistence.Query;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.UserDetails_V004;

public class HibernateTest_V004 {

    static SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();

    public static void createTestUsers() {
        /* Create some users */
        Session session = sessionFactory.openSession();
        session.beginTransaction();
        for (int i = 0; i < 10; i++) {
            UserDetails_V004 user = new UserDetails_V004();
            user.setUserName("user" + i);
            session.save(user);
        }
        session.getTransaction().commit();
        session.close();
        session = null;
    }

    public static void main(String[] args) {
        createTestUsers();

        /* Here although we are getting two user objects but hibernate knows that both the same object
         * because of the id. So hibernate only does one SQL query.
         * so for user1 and user2 hibernate does only one query. but for user3 because its a different session
         * hibernate will do a separate query. We will try to cache that. */

        /* With all the cache settings done following code will only do one select call */
        System.out.println("--------------------session1--------------------------");
        Session session = sessionFactory.openSession();
        session.beginTransaction();
        UserDetails_V004 user1 = (UserDetails_V004) session.get(UserDetails_V004.class, 1);
        UserDetails_V004 user2 = (UserDetails_V004) session.get(UserDetails_V004.class, 1);
        session.getTransaction().commit();
        session.close();

        System.out.println("--------------------session2--------------------------");
        Session session2 = sessionFactory.openSession();
        session2.beginTransaction();
        UserDetails_V004 user3 = (UserDetails_V004) session2.get(UserDetails_V004.class, 1);
        session2.getTransaction().commit();
        session2.close();

        System.out.println(user1 + "\n" + user2 + "\n" + user3);
        /* With cache enabled in above case it does not do even a single select statement as user with
         * id =1 is still in it's cache because of the createTestUsers() */

        /*--------------------------------------------------------
         * Query caching
         --------------------------------------------------------*/
        System.out.println("--------------------session3--------------------------");
        Session session3 = sessionFactory.openSession();
        session3.beginTransaction();
        List<UserDetails_V004> userList1 = session3.createQuery("from USER_DETAILS where userId = 1")
                .setHint("org.hibernate.cacheable", "true").getResultList();
        System.out.println(userList1.toString());
        session3.getTransaction().commit();
        session3.close();

        System.out.println("--------------------session4--------------------------");
        Session session4 = sessionFactory.openSession();
        session4.beginTransaction();
        List<UserDetails_V004> userList2 = session3.createQuery("from USER_DETAILS where userId = 1")
                .setHint("org.hibernate.cacheable", "true").getResultList();
        System.out.println(userList2.toString());
        session4.getTransaction().commit();
        session4.close();

        sessionFactory.close();
    }
}
