package exercises;

//Main file for FHarrayList vs. ArrayList
//CS 1C, Foothill College, Michael Loceff, creator

import java.util.*;
import java.text.*;
import cs_1c.*;

//------------------------------------------------------
public class ArrayListVsFHArrayList
{
// -------  main --------------
public static void main(String[] args) throws Exception
{
   int ARRAY_SIZE = 10000000;
   int SMALL_ARRAY_SIZE = 10000;
   int k, mid, last;
   double avg;
   
   // for timing:
   long start_time, end_time;
   NumberFormat tidy = NumberFormat.getInstance(Locale.US);
   tidy.setMaximumFractionDigits(4);

   // ArrayList using add() / get()
   ArrayList<Integer> list_of_ints = new ArrayList<Integer>(ARRAY_SIZE);
   // START TIME -------------------------------
   start_time = System.nanoTime();
   for (k = 0; k < ARRAY_SIZE; k++)
      list_of_ints.add( (int)(Math.random()*100) );
   
   for (k = 0, avg = 0.; k < ARRAY_SIZE; k++)
      avg += list_of_ints.get(k);
   avg/=ARRAY_SIZE;

   System.out.println("Average: " + avg );
   // end timing
   end_time = System.nanoTime();

   // report algorithm time
   System.out.println("\nElapsed time for ArrayList add/get "
      + tidy.format((end_time - start_time) / 1e9)
      + " seconds.\n");
   
   // FHarrayList using add() / get()
   FHarrayList<Integer> FHlist_of_ints = new FHarrayList<Integer>(ARRAY_SIZE);
   // START TIME -------------------------------
   start_time = System.nanoTime();
   for (k = 0; k < ARRAY_SIZE; k++)
      FHlist_of_ints.add( (int)(Math.random()*100) );
   
   for (k = 0, avg = 0.; k < ARRAY_SIZE; k++)
      avg += FHlist_of_ints.get(k);
   avg/=ARRAY_SIZE;

   System.out.println("Average: " + avg );
   // end timing
   end_time = System.nanoTime();

   // report algorithm time
   System.out.println("\nElapsed time for FHarrayList add/get "
      + tidy.format((end_time - start_time) / 1e9)
      + " seconds.\n");
   
   // ArrayList using set() / get()
   // START TIME -------------------------------
   start_time = System.nanoTime();
   for (k = 0; k < ARRAY_SIZE; k++)
      list_of_ints.set(k, (int)(Math.random()*100) );
   
   for (k = 0, avg = 0.; k < ARRAY_SIZE; k++)
      avg += list_of_ints.get(k);
   avg/=ARRAY_SIZE;

   System.out.println("Average: " + avg );
   // end timing
   end_time = System.nanoTime();

   // report algorithm time
   System.out.println("\nElapsed time for ArrayList set/get "
      + tidy.format((end_time - start_time) / 1e9)
      + " seconds.\n");

   // FHarrayList using set() / get()
   // START TIME -------------------------------
   start_time = System.nanoTime();
   for (k = 0; k < ARRAY_SIZE; k++)
      FHlist_of_ints.set(k, (int)(Math.random()*100) );
   
   for (k = 0, avg = 0.; k < ARRAY_SIZE; k++)
      avg += FHlist_of_ints.get(k);
   avg/=ARRAY_SIZE;

   System.out.println("Average: " + avg );
   // end timing
   end_time = System.nanoTime();

   // report algorithm time
   System.out.println("\nElapsed time for FHarrayList set/get "
      + tidy.format((end_time - start_time) / 1e9)
      + " seconds.\n");
   
   // ArrayList using remove( size - 1 )
   // START TIME -------------------------------
   start_time = System.nanoTime();
   
   while ( ( last = list_of_ints.size() ) > SMALL_ARRAY_SIZE )
      list_of_ints.remove( last - 1 );
   
   // end timing
   end_time = System.nanoTime();
   // report algorithm time
   System.out.println("\nElapsed time for ArrayList remove(size) "
      + tidy.format((end_time - start_time) / 1e9)
      + " seconds.\n");
   
   
   // ArrayList using remove( size - 1 )
   // START TIME -------------------------------
   start_time = System.nanoTime();
   
   while ( ( last = FHlist_of_ints.size() ) > SMALL_ARRAY_SIZE )
      FHlist_of_ints.remove( last - 1 );
   
   // end timing
   end_time = System.nanoTime();
   // report algorithm time
   System.out.println("\nElapsed time for FHarrayList remove(size) "
      + tidy.format((end_time - start_time) / 1e9)
      + " seconds.\n");
   
   // ArrayList using remove( size/2 )
   // START TIME -------------------------------
   start_time = System.nanoTime();
   
   while ( ( mid = list_of_ints.size()/2 ) > 0)
      list_of_ints.remove( mid );

   System.out.println("Average: " + avg );
   // end timing
   end_time = System.nanoTime();

   // report algorithm time
   System.out.println("\nElapsed time for ArrayList remove(size/2) "
      + tidy.format((end_time - start_time) / 1e9)
      + " seconds.\n");

   // FHarrayList using remove( size/2 )
   // START TIME -------------------------------
   start_time = System.nanoTime();
   
   while ( ( mid = FHlist_of_ints.size()/2 ) > 0)
      FHlist_of_ints.remove( mid );

   System.out.println("Average: " + avg );
   // end timing
   end_time = System.nanoTime();

   // report algorithm time
   System.out.println("\nElapsed time for FHarrayList remove(size/2) "
      + tidy.format((end_time - start_time) / 1e9)
      + " seconds.\n");
}
}

/* --- run 10,000,000 add/set/get, 10,000 remove(size/2) --------

Average: 49.5022125

Elapsed time for ArrayList add/get 0.6927 seconds.

Average: 49.4997426

Elapsed time for FHarrayList add/get 0.7502 seconds.

Average: 49.5186798

Elapsed time for ArrayList set/get 0.6651 seconds.

Average: 49.4900174

Elapsed time for FHarrayList set/get 0.6773 seconds.


Elapsed time for ArrayList remove(size) 0.1076 seconds.


Elapsed time for FHarrayList remove(size) 0.2099 seconds.

Average: 49.4900174

Elapsed time for ArrayList remove(size/2) 0.0273 seconds.

Average: 49.4900174

Elapsed time for FHarrayList remove(size/2) 0.0274 seconds.

---------------------------------------------------------- */