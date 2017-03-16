package exercises;

import java.util.*;
import cs_1c.*;

public class LinkedListTest1
{
   public static void main (String[] args)
   {
      int k;
      FHlinkedList<Integer> fh_list = new FHlinkedList<Integer>();

      fh_list.addLast(1);
      fh_list.addLast(2);
      fh_list.addLast(3);
      fh_list.addLast(4);
      fh_list.addLast(5);
      fh_list.addLast(6);

      fh_list.addFirst(0);
      fh_list.addFirst(-1);
      fh_list.addFirst(-2);
      fh_list.addFirst(-3);

      fh_list.set( fh_list.size()/2, -99);
      
      System.out.println( "List size: " + fh_list.size() );
      System.out.println( "First val: " + fh_list.get(0) );
      System.out.println( "Middle val: " + fh_list.get(fh_list.size()/2) );
      System.out.println( "Last val: " + fh_list.get( fh_list.size() - 1) );

      System.out.println( "List size: " + fh_list.size() );
      for (k = 0; k < 4; k++)
      {
         System.out.println( fh_list.getFirst() + " " + fh_list.getLast() );
         fh_list.removeFirst();
      }
      System.out.println("\n" + fh_list.size() );
      for (k = 0; k < 12; k++)
      {
         try
         {
            System.out.println( fh_list.getFirst() + " " + fh_list.removeLast() );
         }
         catch ( NoSuchElementException e)
         {
            System.out.println("Caught Ex. at k = " + k + ".  Empty list.");
         }
      }
      System.out.println( "List size: " + fh_list.size() );
   }
}

/* -------------------- run ----------------------------

List size: 10
First val: -3
Middle val: -99
Last val: 6
List size: 10
-3 6
-2 6
-1 6
0 6

6
1 6
1 5
1 4
1 3
1 -99
1 1
Caught Ex. at k = 6.  Empty list.
Caught Ex. at k = 7.  Empty list.
Caught Ex. at k = 8.  Empty list.
Caught Ex. at k = 9.  Empty list.
Caught Ex. at k = 10.  Empty list.
Caught Ex. at k = 11.  Empty list.
List size: 0


------------------------------------------------------ */