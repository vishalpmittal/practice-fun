package exercises;

import cs_1c.*;
import java.util.*;

public class LinkedListTest2
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
      
      FHlinkedList<String> 
         my_strings = new FHlinkedList<String>(),
         my_strings2 = new FHlinkedList<String>(),
         my_strings3;
      FHlinkedList<Integer> 
         my_ints = new FHlinkedList<Integer>(),
         my_ints2;
      
         
      LinkedList<Integer> my_ints_coll = new LinkedList<Integer>();
      //FHlinkedList<Integer> my_ints_coll = new FHlinkedList<Integer>();
      
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
      my_strings3 = (FHlinkedList<String>)my_strings.clone();
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
      my_ints2 = new FHlinkedList<Integer>();
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

/* -------------------- run ----------------------------

Average: 49.0808
Average: 49.1052

Test as equal -- GOOD
Test as unequal -- GOOD
Test as unequal -- GOOD
clone should test equal -- GOOD
shallow changes after clone
0: When / When
1: Harry / Harry
2: Met / Met
3: Bullitt / The Kennedys

Original String ArrayList:
0: When / 1: Harry / 2: Met / 3: Bullitt / 4: X / 5: Wild / 6: Beast / 7: X / 8:
 X / 9: Men / 10: Nikita / 11: X / 12: Back / 13: To / 14: The / 15: Future / 16
: X / 17: House / 18: Good / 19: Wife / 
Item added in position 2:
0: When / 1: Harry / 2: Broken Heart / 3: Met / 4: Bullitt / 5: X / 6: Wild / 7:
 Beast / 8: X / 9: X / 10: Men / 11: Nikita / 12: X / 13: Back / 14: To / 15: Th
e / 16: Future / 17: X / 18: House / 19: Good / 20: Wife / 

Testing remove(index) and remove(object).
0: 49 / 1: 37 / 2: 37 / 3: 18 / 4: 74 / 5: 13 / 
0th and 3rd items should be gone.
0: 37 / 1: 37 / 2: 74 / 3: 13 / 4: 33 / 5: 51 / 

New size (should be 0): 0

addAll() -- should be identical
0: 0 / 1: 1 / 2: 2 / 3: 3 / 4: 4 / 5: 5 / 6: 6 / 7: 7 / 8: 8 / 9: 9 / 
0: 0 / 1: 1 / 2: 2 / 3: 3 / 4: 4 / 5: 5 / 6: 6 / 7: 7 / 8: 8 / 9: 9 / 

0: 0 / 1: 1 / 2: 2 / 3: 3 / 4: 4 / 5: 5 / 6: 2 / 7: 6 / 8: 7 / 9: 8 / 10: 9 / 

indexOf() and lastIndexOf()
index of 2: 2
last index of 2: 6

String List contains Bullitt? (should be T): true
Int List contains 93? (should be F): false

set() - caught!  -- java.lang.IndexOutOfBoundsException
add() - caught!  -- java.lang.IndexOutOfBoundsException
get() - caught!  -- java.lang.IndexOutOfBoundsException

Testing toArray()
0: When / 1: Harry / 2: Broken Heart / 3: Met / 4: Bullitt / 5: X / 6: Wild / 7:
 Beast / 8: X / 9: X / 10: Men / 11: Nikita / 12: X / 13: Back / 14: To / 15: Th
e / 16: Future / 17: X / 18: House / 19: Good / 20: Wife / 
0: When / 1: Harry / 2: Broken Heart / 3: Met / 4: Bullitt / 5: X / 6: Wild / 7:
 Beast / 8: X / 9: X / 10: Men / 11: Nikita / 12: X / 13: Back / 14: To / 15: Th
e / 16: Future / 17: X / 18: House / 19: Good / 20: Wife / 
*/
//-----------------------------------------------------