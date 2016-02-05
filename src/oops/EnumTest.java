package oops;

public class EnumTest{
	public static void test(){
		Day d = Day.MONDAY;
		Day1 d1 = Day1.MONDAY;
	}
}

class Day{
	//private instance variable
	private String name;
	
	//private constructor, can not be instantiated 
	private Day (String name){ this.name = name; }
	
	//static and final object references of self type
	public static final Day MONDAY = new Day("Monday");
	public static final Day TUESDAY = new Day("Tuesday");
	public static final Day WEDNESDAY = new Day("Wednesday");
	public static final Day THURSDAY = new Day("Thursday");
	public static final Day FRIDAY = new Day("Friday");
	public static final Day SATURDAY = new Day("Saturday");
	public static final Day SUNDAY = new Day("Friday");
	
	public String getName(){ return name; }	
}

// By default its final so no need to mention
enum Day1{
	// These should be always first line in the class
	// By default all of these are publid static final and are of type oops.Day1
	MONDAY("Monday"),TUESDAY("Tuesday"),WEDNESDAY("Wednesday"),THURSDAY("Thursday"),FRIDAY("Friday"),SATURDAY("Saturday"),SUNDAY("Friday"),HOLIDAY();
	
	public String name;
	
	// constructor is by default private and public is not allowed
	Day1(String name){
		this.name=name;
	}
	
	// can have any number of constructors but all would be private
	Day1(){
		this.name="Holiday";
	}
	
	public String getName(){ return name; }
}
