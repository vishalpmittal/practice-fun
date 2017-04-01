package dto;

import java.util.Date;
import java.util.HashSet;
import java.util.Set;

import javax.persistence.Column;
import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.Table;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;

@Entity
@Table(name = "USER_DETAILS")
public class UserDetails_V5 {

    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    @Column(name = "USER_ID")
    private int userId;

    @Column(name = "USER_NAME")
    private String userName;

    /* Address class is marked as @Embeddable and now
     * the collection of Addresses is marked as "ElementCollection for hibernate to persist
     * the object */

    /* Hibernate: drop table hibernate_sequence
     * Hibernate: drop table USER_DETAILS
     * Hibernate: drop table UserDetails_V5_listOfAddresses
     * Hibernate: create table hibernate_sequence (next_val numeric)
     * Hibernate: insert into hibernate_sequence values ( 1 )
     * 
     * Hibernate: create table USER_DETAILS (USER_ID integer not null, JOIN_DATE date, USER_NAME varchar(255), primary
     * key (USER_ID))
     * 
     * Hibernate: create table UserDetails_V5_listOfAddresses (UserDetails_V5_USER_ID integer not null, CITY_NAME
     * varchar(255), PIN_CODE varchar(255), STATE_NAME varchar(255), STREET_NAME varchar(255))
     * 
     * Hibernate: select next_val as id_val from hibernate_sequence for update
     * Hibernate: update hibernate_sequence set next_val= ? where next_val=?
     * Hibernate: insert into USER_DETAILS (JOIN_DATE, USER_NAME, USER_ID) values (?, ?, ?)
     * 
     * Hibernate: insert into UserDetails_V5_listOfAddresses (UserDetails_V5_USER_ID, CITY_NAME, PIN_CODE, STATE_NAME,
     * STREET_NAME) values (?, ?, ?, ?, ?)
     * 
     * Hibernate: insert into UserDetails_V5_listOfAddresses (UserDetails_V5_USER_ID, CITY_NAME, PIN_CODE, STATE_NAME,
     * STREET_NAME) values (?, ?, ?, ?, ?) */

    /* Basically it used user IDs as foreign keys and added them to each row in UserDetails_V5_listOfAddresses table for
     * mapping */
    @ElementCollection

    /* Changes the address table name to USER_ADDRESS
     * Changes the join reference key column name to USER_ID */
    @JoinTable(name = "USER_ADDRESS", joinColumns = @JoinColumn(name = "USER_ID"))
    private Set<Address_V5> listOfAddresses = new HashSet<Address_V5>();

    @Temporal(TemporalType.DATE)
    @Column(name = "JOIN_DATE")
    private Date joinedDate;

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public Date getJoinedDate() {
        return joinedDate;
    }

    public void setJoinedDate(Date joinedDate) {
        this.joinedDate = joinedDate;
    }

    public Set<Address_V5> getListOfAddresses() {
        return listOfAddresses;
    }

    public void setListOfAddresses(Set<Address_V5> listOfAddresses) {
        this.listOfAddresses = listOfAddresses;
    }

}
