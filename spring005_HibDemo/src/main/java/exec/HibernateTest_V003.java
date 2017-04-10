package exec;

import java.util.List;

import javax.persistence.Query;

import org.hibernate.Criteria;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.hibernate.criterion.Example;
import org.hibernate.criterion.Order;
import org.hibernate.criterion.Projections;
import org.hibernate.criterion.Restrictions;

import dto.UserDetails_V003;

public class HibernateTest_V003 {
    static SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();

    public static void createTestUsers() {
        /* Create some users */
        Session session = sessionFactory.openSession();
        session.beginTransaction();
        for (int i = 0; i < 10; i++) {
            UserDetails_V003 user = new UserDetails_V003();
            user.setUserName("user" + i);
            session.save(user);
        }
        session.getTransaction().commit();
        session.close();
        session = null;
    }

    public static void main(String[] args) {
        createTestUsers();

        Session session = sessionFactory.openSession();
        session.beginTransaction();

        /* ------------------------------------------
         * Select and Pagination
         * ------------------------------------------ */
        /* grab 4 records starting record number 5 */
        Query query = session.createQuery("from USER_DETAILS");
        query.setFirstResult(5);
        query.setMaxResults(4);

        List<UserDetails_V003> users = (List<UserDetails_V003>) query.getResultList();
        System.out.println(users.size() + " users: \n" + users);

        /* select only some field from the userdetail object */
        query = session.createQuery("SELECT userName from USER_DETAILS");
        List<String> userNames = (List<String>) query.getResultList();
        System.out.println("All user names: " + userNames);

        /* returns a list of list */
        query = session.createQuery("SELECT userId, userName from USER_DETAILS");

        /* returns a list of map objects where each member is a map */
        query = session.createQuery("SELECT new map(userId, userName) from USER_DETAILS");

        /* works with aggregation functions max, min, sum, etc. */
        query = session.createQuery("SELECT max(userId) from USER_DETAILS");

        /* ------------------------------------------
         * Understanding Parameter Binding and SQL Injection
         * ------------------------------------------ */
        /* not very good way because if someone gets access to minUserId it can be modified to
         * minUserId = "5 or 1 == 1"
         * minUserId = "5 or true"
         * the query is going to return all the users which is not acceptable */
        String minUserId = "5";
        query = session.createQuery("from USER_DETAILS where userId > " + minUserId);
        users = (List<UserDetails_V003>) query.getResultList();
        System.out.println(users.size() + " users: \n" + users);

        /* A better way of doing the above thing */
        String userName = "user1";
        query = session.createQuery("from USER_DETAILS where userId = ? OR userName = ?");
        query.setParameter(0, Integer.parseInt(minUserId));
        query.setParameter(1, userName);
        users = (List<UserDetails_V003>) query.getResultList();
        System.out.println(users.size() + " users: \n" + users);

        /* Even better way of doing the above thing */
        userName = "user1";
        query = session.createQuery("from USER_DETAILS where userId = :userId OR userName = :userName");
        query.setParameter("userId", Integer.parseInt(minUserId));
        query.setParameter("userName", userName);
        users = (List<UserDetails_V003>) query.getResultList();
        System.out.println(users.size() + " users: \n" + users);

        /* ------------------------------------------
         * Named Queries
         * ------------------------------------------ */
        query = session.getNamedQuery("userDetails.byId");
        query.setParameter("userId", Integer.parseInt(minUserId));
        users = (List<UserDetails_V003>) query.getResultList();
        System.out.println(users.size() + " users: \n" + users);

        /* ------------------------------------------
         * Named Native Queries (Full sql statement)
         * ------------------------------------------ */
        query = session.getNamedNativeQuery("userDetails.byName");
        query.setParameter("userName", userName);
        users = (List<UserDetails_V003>) query.getResultList();
        System.out.println(users.size() + " users: \n" + users);

        /* ------------------------------------------
         * Criteria APIs
         * ------------------------------------------ */
        Criteria criteria = session.createCriteria(UserDetails_V003.class);
        criteria.add(Restrictions.eq("userName", "user8"));
        users = (List<UserDetails_V003>) criteria.list();
        System.out.println("Criteria APIs \n" + users.size() + " users: \n" + users);

        /* ------------------------------------------
         * Restrictions
         * ------------------------------------------ */
        criteria = session.createCriteria(UserDetails_V003.class);
        criteria.add(Restrictions.like("userName", "%user%")).add(Restrictions.gt("userId", 4))
                .add(Restrictions.between("userId", 6, 8));
        users = (List<UserDetails_V003>) criteria.list();
        System.out.println("Restrictions1 \n" + users.size() + " users: \n" + users);

        criteria = session.createCriteria(UserDetails_V003.class);
        criteria.add(Restrictions.or(Restrictions.lt("userId", 3), Restrictions.between("userId", 6, 8)));
        users = (List<UserDetails_V003>) criteria.list();
        System.out.println("Restrictions2 Or condition \n" + users.size() + " users: \n" + users);

        /* ------------------------------------------
         * Projections
         * ------------------------------------------ */
        // returns just the user ids of all users
        criteria = session.createCriteria(UserDetails_V003.class).setProjection(Projections.property("userId"));
        users = (List<UserDetails_V003>) criteria.list();
        System.out.println("Projections1: \n" + users.size() + " users: \n" + users);

        // return the count of users
        // can be used with other aggregation funtions like "distict, avg, countDisticnt, min, max, sum"
        criteria = session.createCriteria(UserDetails_V003.class).setProjection(Projections.count("userId"));
        users = (List<UserDetails_V003>) criteria.list();
        System.out.println("Projections2: \n" + users.size() + " users: \n" + users);

        // setting the order, sorting.
        criteria = session.createCriteria(UserDetails_V003.class).setProjection(Projections.property("userId"))
                .addOrder(Order.desc("userId"));
        users = (List<UserDetails_V003>) criteria.list();
        System.out.println("Projections3: \n" + users.size() + " users: \n" + users);

        /* ------------------------------------------
         * Query by example, does not consider primary keys and nulls, but other fields are okay
         * ------------------------------------------ */
        UserDetails_V003 exUser = new UserDetails_V003();
        exUser.setUserName("user5");
        Example ex = Example.create(exUser);
        criteria = session.createCriteria(UserDetails_V003.class).add(ex);
        users = (List<UserDetails_V003>) criteria.list();
        System.out.println("Example 1: \n" + users.size() + " users: \n" + users);

        // will return user1, user10, etc
        exUser = new UserDetails_V003();
        exUser.setUserName("user1%");
        ex = Example.create(exUser).enableLike();
        criteria = session.createCriteria(UserDetails_V003.class).add(ex);
        users = (List<UserDetails_V003>) criteria.list();
        System.out.println("Example 1: \n" + users.size() + " users: \n" + users);

        session.getTransaction().commit();
        session.close();
        sessionFactory.close();

    }
}
