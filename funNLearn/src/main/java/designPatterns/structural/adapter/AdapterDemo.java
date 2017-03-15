package designPatterns.structural.adapter;

import java.util.List;

import designPatterns.structural.adapter.base.Employee;

public class AdapterDemo {

	public static void main(String[] args) {
		EmployeeClient client = new EmployeeClient();
		
		List<Employee> employees = client.getEmployeeList();
		
		System.out.println(employees);
	}
}
