package exercises;

import java.text.NumberFormat;
import java.util.*;
import cs_1c.*;

public class LinkedListTimingTest
{
   // -------  main --------------
   public static void main(String[] args) throws Exception
   {
      int SIZE = 2000000;
      int k;
      
      // for timing:
      long start_time, end_time;
      NumberFormat tidy = NumberFormat.getInstance(Locale.US);
      tidy.setMaximumFractionDigits(4);

      System.out.println("\nList size: " + SIZE);
      
      // LinkedList
      LinkedList<Integer> list_of_ints = new LinkedList<Integer>();
      // START TIME -------------------------------
      start_time = System.nanoTime();
      for (k = 0; k < SIZE; k++)
      {
         list_of_ints.addFirst(-k);
         list_of_ints.addLast(k);
      }
      for (k = 0; k < SIZE; k++)
      {
         list_of_ints.getFirst();  list_of_ints.getLast();
         list_of_ints.removeFirst();
         list_of_ints.removeLast();
      }
      // end timing
      end_time = System.nanoTime();
      
      // report algorithm time
      System.out.println("\nElapsed time for LinkedList: "
         + tidy.format((end_time - start_time) / 1e9)
         + " seconds.");

      // FHlinkedList
      FHlinkedList<Integer> FHlist_of_ints = new FHlinkedList<Integer>();
      // START TIME -------------------------------
      start_time = System.nanoTime();
      for (k = 0; k < SIZE; k++)
      {
         FHlist_of_ints.addFirst(-k);
         FHlist_of_ints.addLast(k);
      }
      for (k = 0; k < SIZE; k++)
      {
         FHlist_of_ints.getFirst();  FHlist_of_ints.getLast();
         FHlist_of_ints.removeFirst();
         FHlist_of_ints.removeLast();
      }
      // end timing
      end_time = System.nanoTime();
      
      System.out.println("\nElapsed time for FHlinkedList: "
            + tidy.format((end_time - start_time) / 1e9)
            + " seconds.");
   }
}

/* ---------------------- RUNS ------------------------------
List size: 200000

Elapsed time for LinkedList: 0.1385 seconds.

Elapsed time for FHlinkedList: 0.1278 seconds.

----------------------
List size: 2000000

Elapsed time for LinkedList: 1.6313 seconds.

Elapsed time for FHlinkedList: 0.5857 seconds.
------------------------------------------------------------ */