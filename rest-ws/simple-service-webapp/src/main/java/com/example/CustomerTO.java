package com.example;

import java.util.Date;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class CustomerTO {
    public String name;
    public Long creditLimit;
    public Date customerSince;

//    public CustomerTO(String name, Long creditLimit, Date customerSince) {
//        this.name = name;
//        this.creditLimit = creditLimit;
//        this.customerSince = customerSince;
//    }

    public CustomerTO(Customer c) {
        this.name = c.getName();
        this.creditLimit = c.getCreditLimit();
        this.customerSince = c.getCustomerSince();
    }
    
    public CustomerTO() {} // for JAX-B and JSON input
    
    @Override
    public String toString() {
        return "CustomerTO{" + "name=" + name + ", creditLimit=" + creditLimit + ", customerSince=" + customerSince + '}';
    }
}