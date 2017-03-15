package designPatterns.creational.prototype.exmple1;

import java.util.ArrayList;
import java.util.List;

public class PrototypeDemo {
	public static void main(String args[]) {

		String sql = "select * from movies where tile = ?";
		
		List<String> parameters = new ArrayList<String>();
		parameters.add("Star wars");
		
		Record record = new Record();

		Statement firstStatment = new Statement(sql, parameters, record);
		System.out.println(firstStatment.getSql());
		System.out.println(firstStatment.getParameters());
		System.out.println(firstStatment.getRecord());

		Statement secondStatment = firstStatment.clone();
		System.out.println(secondStatment.getSql());
		System.out.println(secondStatment.getParameters());
		System.out.println(secondStatment.getRecord());
	}
}
