package exercises;
// Main file for iTunes project - insertion example.
// CS 1C, Foothill College, Michael Loceff, creator

import cs_1c.*;
import java.util.*;
import java.text.*;

//------------------------------------------------------
public class InsertTiming
{
   // -------  main --------------
   public static void main(String[] args) throws Exception
   {
      // to time the algorithm -------------------------
      long start_time, end_time;
      NumberFormat tidy = NumberFormat.getInstance(Locale.US);
      tidy.setMaximumFractionDigits(4);

      // how we read the data from files
      iTunesEntryReader tunes_input = new iTunesEntryReader("itunes_file.txt");
      int array_size;

      // how we test the success of the read:
      if (tunes_input.readError())
      {
         System.out.println("couldn't open " + tunes_input.getFileName()
            + " for input.");
         return;
      }

      // create an array of objects for our own use:
      array_size = tunes_input.getNumTunes();
      // we add 1 to make room for an insertion
      iTunesEntry[] tunes_array = new iTunesEntry[array_size + 1];
      for (int k = 0; k < array_size; k++)
         tunes_array[k] = tunes_input.getTune(k);

      // 5 positions we will insert at in the larger iTunes list of 80 tunes
      int write_position;
      final int NUM_INSERTIONS  = 5000000;
      int[] some_positions = {3, 67, 20, 15, 59  };

      int num_positions = some_positions.length;

      System.out.println("Doing " + NUM_INSERTIONS  + " insertions in array having "
         + array_size + " iTunes." );

      
      //get start time
      start_time = System.nanoTime();
      
      // we will do NUM_INSERTIONS insertions, throwing away tunes that run off the top
      for (int attempt = 0; attempt < NUM_INSERTIONS; attempt++)
      {
         write_position = some_positions[ attempt % num_positions ];

         // move everything up one 
         for (int k = array_size; k > write_position; k--)
            tunes_array[k] = tunes_array[k-1];

         // now put a new tune into the free position
         tunes_array[write_position].setSArtist("Amerie");
         tunes_array[write_position].setSTitle("Outro");
         tunes_array[write_position].setNTime(63);
      }

      // how we determine the time elapsed -------------------
      end_time = System.nanoTime();

      // report algorithm time
      System.out.println("\nAlgorithm Elapsed Time: "
         + tidy.format((end_time - start_time) / 1e9)
         + " seconds.\n");
   }
}

/* ---------------- Runs -------------------

Doing 5000000 insertions in array having 79 iTunes.

Algorithm Elapsed Time: 1.2814 seconds.

---------

Doing 500000 insertions in array having 79 iTunes.

Algorithm Elapsed Time: 0.1684 seconds.

---------

Doing 50000 insertions in array having 79 iTunes.

Algorithm Elapsed Time: 0.0271 seconds.

---------

Doing 5000 insertions in array having 79 iTunes.

Algorithm Elapsed Time: 0.0031 seconds.

---------

Doing 500 insertions in array having 79 iTunes.

Algorithm Elapsed Time: 0.0011 seconds.

---------

Doing 50 insertions in array having 79 iTunes.

Algorithm Elapsed Time: 0.0001 seconds.

---------------------------------------- */