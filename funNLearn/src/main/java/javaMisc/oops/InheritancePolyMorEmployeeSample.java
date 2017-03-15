package javaMisc.oops;

class Employee
{
   public String name = "John";
   public int salary =  100;
   public String work()
   {
     return"oops.Employee Working";
   }
}

class Manager extends Employee
{  
   public String product = "scjp";
   public int salary = 200;
   public String work()
   {
      return ("oops.Manager Working");
   }
   public String manage()
   {
      return "Managing product";
   }
}

public class InheritancePolyMorEmployeeSample 
{
   public static void main(String arg[])
   {
	  //===========Assignment test==========
	  // regular assignment
	  Employee e1 = new Employee();
      System.out.println(e1.name + ", " + e1.salary + ", "+ e1.work());    //John, 100, oops.Employee Working
      //System.out.println(e1.product + ", " + e1.manage());               //Compilation error, e1 does not have product and manage()
      
      //Assigning subclass manager object to superclass employee reference
      Employee e2 = new Manager();
      System.out.println(e2.name + ", " + e2.salary + ", "+ e2.work());    //John, 100, oops.Manager Working
      //System.out.println(e2.product + ", " + e2.manage());               //Compilation error, e2 does not have product and manage()
      
      //regular assignment, compiles and run fine
      Manager m1 = new Manager();
      System.out.println(m1.name + ", " + m1.salary + ", "+ m1.work());    //John, 200, oops.Manager Working
      System.out.println(m1.product + ", " + m1.manage());                 //scjp, Managing product
      
      //=======compilation error : can not assign superclass object to subclass type======= 
      // oops.Manager m2 = new oops.Employee();
      
      //=======Casting test=======
      // This give run time exception because e1 is defined as e1 = new oops.Employee()
      // Exception in thread "main" java.lang.ClassCastException: oops.Employee
      // cannot be cast to oops.Manager
      // oops.Manager m3 = (oops.Manager) e1;
      
      // This compiles fine because e2 is defined as e2 = new oops.Manager()
      Manager m4 = (Manager) e2;
      System.out.println(m4.name + ", " + m4.salary + ", "+ m4.work());    //John, 200, oops.Manager Working
      System.out.println(m4.product + ", " + m4.manage());                 //scjp, Managing product
      
      // This compiles and runs fine as upcasting is allowed in any case
      Employee e3 = (Employee) m1;
      System.out.println(e3.name + ", " + e3.salary + ", "+ e3.work());    //John, 100, oops.Manager Working
      //System.out.println(e3.product + ", " + e3.manage());               //Compilation error, e3 does not have product and manage()
   }
}
