package designPatterns.structural.adapter;

import java.util.ArrayList;
import java.util.List;

import designPatterns.structural.adapter.base.Employee;
import designPatterns.structural.adapter.base.EmployeeDB;
import designPatterns.structural.adapter.thridParty.EmployeeCSV;
import designPatterns.structural.adapter.thridParty.EmployeeLdap;

public class EmployeeClient {

    public List<Employee> getEmployeeList() {

        List<Employee> employees = new ArrayList<Employee>();

        Employee employeeFromDB = new EmployeeDB("1234", "John", "Wick", "john@wick.com");

        employees.add(employeeFromDB);

        // Will not work! This is where the adapter comes into play!

        // Employee employeeFromLdap = new EmployeeLdap("chewie", "Solo", "Han", "han@solo.com");

        EmployeeLdap employeeFromLdap = new EmployeeLdap("chewie", "Solo", "Han", "han@solo.com");

        employees.add(new EmployeeAdapterLdap(employeeFromLdap));

        EmployeeCSV employeeFromCSV = new EmployeeCSV("567,Sherlock,Holmes,sherlock@holmes.com");

        employees.add(new EmployeeAdapterCSV(employeeFromCSV));

        return employees;

    }

}
