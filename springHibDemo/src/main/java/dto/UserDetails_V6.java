package dto;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;
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

import org.hibernate.annotations.CollectionId;
import org.hibernate.annotations.GenericGenerator;
import org.hibernate.annotations.Type;

@Entity
@Table(name = "USER_DETAILS")
public class UserDetails_V6 {

    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    @Column(name = "USER_ID")
    private int userId;

    @Column(name = "USER_NAME")
    private String userName;

    @ElementCollection
    @JoinTable(name = "USER_ADDRESS", joinColumns = @JoinColumn(name = "USER_ID"))

    /* Hibernate specific params
     * In order to have a collection of objects as member variable inside entity class
     * - change the collection type to something that supports indexes, like arrayList
     * - define @CollectionId with all the attributes
     * - @GenericGenerator makes the id to be auto generated and id is long type
     * --------------------------------------------------------
     * In V5 version of the classes the user_id was used as a foreign key in the address table and that was it,
     * but there was no primary key for this USER_ADDRESS table.
     * By adding following annotations a new field call ADDRESS_ID will be added to the USER_ADDRESS table
     * and that will be then used as a primary key of that table
     * -------------------------------------------------------- */
    @GenericGenerator(name = "sequence-gen", strategy = "sequence")
    @CollectionId(columns = { @Column(name = "ADDRESS_ID") }, generator = "sequence-gen", type = @Type(type = "long"))
    private Collection<Address_V6> listOfAddresses = new ArrayList<Address_V6>();

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

    public Collection<Address_V6> getListOfAddresses() {
        return listOfAddresses;
    }

    public void setListOfAddresses(Collection<Address_V6> listOfAddresses) {
        this.listOfAddresses = listOfAddresses;
    }

}
