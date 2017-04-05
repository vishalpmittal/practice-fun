package exec;

import java.util.Date;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.Address_V6;
import dto.UserDetails_V6;

public class HibernateTest_V6 {

    public static void main(String[] args) {
        UserDetails_V6 user1 = new UserDetails_V6();
        user1.setUserName("User1");
        user1.setJoinedDate(new Date());

        Address_V6 add1 = new Address_V6();
        add1.setStreet("100 1st Street");
        add1.setCity("San Jose");
        add1.setState("CA");
        add1.setPincode("12345");

        Address_V6 add2 = new Address_V6();
        add2.setStreet("200 2nd Street");
        add2.setCity("San Jose");
        add2.setState("CA");
        add2.setPincode("23456");

        user1.getListOfAddresses().add(add1);
        user1.getListOfAddresses().add(add2);

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();

        session.save(user1);

        // commit the transaction
        session.getTransaction().commit();
        session.close();

        /* -----------------------------------------------------------------
         * Get the user data back using hibernate
         * ----------------------------------------------------------------- */
        UserDetails_V6 user2 = null;
        session = sessionFactory.openSession();

        // after this command hibernate creates a proxy user object (a proxy user subclass of UserDetails_V6
        // is created internally by hibernate ) and does not grab the whole object
        user2 = (UserDetails_V6) session.get(UserDetails_V6.class, 1);

        // at this command hibernate goes and grab only the data that is needed
        System.out.println(user2.getListOfAddresses().size());
        session.close();

        /* -----------------------------------------------------------------
         * fetching type
         * ----------------------------------------------------------------- */
        UserDetails_V6 user3 = null;
        session = sessionFactory.openSession();
        user3 = (UserDetails_V6) session.get(UserDetails_V6.class, 1);

        session.close();

        // This will fail as at this point only proxy object was present and the session is already closed
        System.out.println(user3.getListOfAddresses().size());

        // to Make it work add following at the top of listOfAddresses in UserDetails_v6
        // @ElementCollection(fetch=FetchType.EAGER)

        sessionFactory.close();
    }
}
