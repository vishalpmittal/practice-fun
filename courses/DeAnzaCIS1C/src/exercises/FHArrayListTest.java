package exercises;

import cs_1c.*;
import java.util.*;

public class FHArrayListTest
{
   public static void main (String[] args) throws CloneNotSupportedException
   {
      int k;
      final int INT_ARRAY_SIZE = 10000;
      double avg;
      
      String[] words = {"When", "Harry", "Met", "Bullitt", 
         "X", "Wild", "Beast", "X", 
         "X", "Men", "Nikita", "X", "Back", "To", 
         "The", "Future", "X", "House", "Good", "Wife"};
      String[] captured_strings = new String[100];
      
      FHarrayList<String> 
         my_strings = new FHarrayList<String>(),
         my_strings2 = new FHarrayList<String>(),
         my_strings3;
      FHarrayList<Integer> 
         my_ints = new FHarrayList<Integer>(INT_ARRAY_SIZE),
         my_ints2;
      FHarrayList<Integer> my_ints_coll = new FHarrayList<Integer>();
      
      
      // testing add() on Strings
      for (k = 0; k < words.length; k++)
      {
         my_strings.add(words[k]);
         my_strings2.add(new String(words[k]));
      }
      
      // testing add(index, ...) on ints
      for (k = 0; k < INT_ARRAY_SIZE; k++)
         my_ints.add( my_ints.size()/2, (int)(Math.random()*100) );

      // testing get() on ints
      for (k = 0, avg = 0.; k < my_ints.size(); k++)
         avg += my_ints.get(k);
      avg/=my_ints.size();
      System.out.println("Average: " + avg );

      // testing set() on ints
      for (k = 0; k < my_ints.size(); k++)
         my_ints.set(k, (int)(Math.random()*100) );
      
      for (k = 0, avg = 0.; k < my_ints.size(); k++)
         avg += my_ints.get(k);
      avg/=my_ints.size();
      System.out.println("Average: " + avg );
      
      // testing equals
      if (my_strings.equals(my_strings2))
         System.out.println("\nTest as equal -- GOOD");
      else
         System.out.println("Test as unequal -- ERROR");

      my_strings2.set(2, "Hurt Locker");
      if (my_strings.equals(my_strings2))
         System.out.println("Test as equal -- ERROR");
      else
         System.out.println("Test as unequal -- GOOD");      

      if (my_strings.equals(my_ints))
         System.out.println("Test as equal -- ERROR");
      else
         System.out.println("Test as unequal -- GOOD");
      
      // testing clone
      my_strings3 = (FHarrayList<String>)my_strings.clone();
      if (my_strings.equals(my_strings3))
         System.out.println("clone should test equal -- GOOD");
      else
         System.out.println("clone tests unequal -- ERROR");
      
      my_strings3.set(3, "The Kennedys");
      System.out.println("shallow changes after clone");
      for (k = 0; k < 4; k++)
         System.out.println(k + ": " + my_strings.get(k) + " / "
               + my_strings3.get(k) ); 
      
      // testing add(index, ...) on Strings
      System.out.println("\nOriginal String ArrayList:"); 
      for (k = 0; k < my_strings.size(); k++)
         System.out.print(k + ": " + my_strings.get(k) + " / ");
      System.out.println(); 
      
      my_strings.add(2, "Broken Heart");
      
      System.out.println("Item added in position 2:"); 
      for (k = 0; k < my_strings.size(); k++)
         System.out.print(k + ": " + my_strings.get(k) + " / ");
      System.out.println(); 
      
      // testing remove(index) and remove(object)
      System.out.println("\nTesting remove(index) and remove(object).");
      for (k = 0; k < 6; k++)
         System.out.print(k + ": " + my_ints.get(k) + " / ");
      System.out.println();
      
      my_ints.remove(3);
      my_ints.remove( my_ints.get(0) );
      
      System.out.println("0th and 3rd items should be gone.");
      for (k = 0; k < 6; k++)
         System.out.print(k + ": " + my_ints.get(k) + " / ");
      System.out.println();
      
      // testing clear() and addAll()
      my_ints.clear();
      System.out.println("\nNew size (should be 0): " + my_ints.size() );
      for (k = 0; k < 10; k++)
         my_ints_coll.add(k);
      my_ints2 = new FHarrayList<Integer>();
      my_ints2.addAll(my_ints_coll);

      System.out.println("\naddAll() -- should be identical");
      for (k = 0; k < my_ints_coll.size(); k++)
         System.out.print(k + ": " + my_ints_coll.get(k) + " / " );
      System.out.println();
      for (k = 0; k < my_ints2.size(); k++)
         System.out.print(k + ": " + my_ints2.get(k) + " / ");
      System.out.println();
      
      // testing indexOf()...
      my_ints2.add(6,2);
      System.out.println();
      for (k = 0; k < my_ints2.size(); k++)
         System.out.print(k + ": " + my_ints2.get(k) + " / ");
      System.out.println();
      System.out.println("\nindexOf() and lastIndexOf()");
      System.out.println("index of 2: " + my_ints2.indexOf(2));    
      System.out.println("last index of 2: " + my_ints2.lastIndexOf(2));  
      System.out.println();
      
      // testing contains()
      System.out.println("String List contains Bullitt? (should be T): " 
            + my_strings.contains("Bullitt") );
      System.out.println("Int List contains 93? (should be F): " 
            + my_ints2.contains(93) ); 
      
      // testing exceptions -----------------
      System.out.println();
      // set()
      try
      {
         my_ints.set(20, 20);
      }
      catch(Exception e)
      {
         System.out.println("set() - caught!  -- " + e);
      }
   
      // add()
      try
      {
         my_ints.add(20, 20);
      }
      catch(Exception e)
      {
         System.out.println("add() - caught!  -- " + e);
      }
    
      // get()
      try
      {
         my_ints.get(20);
      }
      catch(Exception e)
      {
         System.out.println("get() - caught!  -- " + e);
      }
      
      System.out.println("\nTesting toArray()");
      String[] y = my_strings.toArray(captured_strings);
      
      for (k = 0; captured_strings[k] != null; k++)
         System.out.print(k + ": " + captured_strings[k] + " / ");
      System.out.println();
      for (k = 0; y[k] != null; k++)
         System.out.print(k + ": " + y[k] + " / ");
  }
}