package exec;

import java.util.Date;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import dto.Address_V4;
import dto.UserDetails_V4;

public class HibernateTest_V4 {

    public static void main(String[] args) {
        UserDetails_V4 user1 = new UserDetails_V4();
        user1.setUserName("User1");
        user1.setJoinedDate(new Date());
        user1.setDescription("User1 description");
        Address_V4 add1 = new Address_V4();
        add1.setStreet("100 1st Street");
        add1.setCity("San Jose");
        add1.setState("CA");
        add1.setPincode("12345");

        /* The address fields will added as columns in USER_DETAILS table itself
         * The colum names will be
         * STREET_NAME, CITY_NAME, STATE_NAME, PIN_CODE */
        user1.setHomeAddress(add1);

        Address_V4 add2 = new Address_V4();
        add2.setStreet("200 2nd Street");
        add2.setCity("San Jose");
        add2.setState("CA");
        add2.setPincode("23456");

        /* this address will also be added in the same USER_DETAILS table but the column names will be
         * OFFICE_STREET_NAME, OFFICE_CITY_NAME, OFFICE_STATE_NAME, OFFICE_PIN_CODE */

        user1.setOfficeAddress(add2);

        SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
        Session session = sessionFactory.openSession();
        session.beginTransaction();

        // Even though we are not providing ids Hibernate will auto generate it
        session.save(user1);

        // commit the transaction
        session.getTransaction().commit();
        session.close();
        sessionFactory.close();

    }
}
