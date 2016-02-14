/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example;

import java.util.Date;

/**
 *
 * @author simon
 */
public class Customer {
    private String name;
    private Long creditLimit;
    private Date customerSince;

    public String getName() {
        return name;
    }

    public Long getCreditLimit() {
        return creditLimit;
    }

    public Date getCustomerSince() {
        return customerSince;
    }

    public Customer(String name, Long creditLimit, Date customerSince) {
        this.name = name;
        this.creditLimit = creditLimit;
        this.customerSince = customerSince;
    }

    @Override
    public String toString() {
        return "Customer{" + "name=" + name + ", creditLimit=" + creditLimit + ", customerSince=" + customerSince + '}';
    }
}