package exercises;
// Main file for iTunes project - search example.
// CIS CS 1C, Foothill College, Michael Loceff, creator

import cs_1c.*;
import java.util.*;
import java.text.*;

//------------------------------------------------------
public class SearchTiming
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
      iTunesEntry[] tunes_array = new iTunesEntry[array_size];
      for (int k = 0; k < array_size; k++)
         tunes_array[k] = tunes_input.getTune(k);

      // 5 titles we will search for in the larger iTunes list of 80 tunes
      String search_title;
      final int NUM_SEARCHES = 500000;
      String[] some_titles = 
      { 
         "Russian Roulette", 
         "Brahms: Symphony No. 1 in C Minor Op. 68",
         "Give It All U Got",
         "A Love Supreme Part 1",
         "Something to Talk About"
      };
      int num_titles = some_titles.length;

      System.out.println("Doing " + NUM_SEARCHES + " searches in array having "
         + array_size + " iTunes." );
      
      //get start time
      start_time = System.nanoTime();
      
      // we will do NUM_SEARCHES searches
      for (int attempt = 0; attempt < NUM_SEARCHES; attempt++)
      {
         search_title = some_titles[ attempt % num_titles ];
         for (int k = 0; k < array_size; k++)
         {
            if (tunes_array[k].getSTitle().equals(search_title))
            {
               // only print out to see that the searches work
               // then we remove for timing
               // System.out.println("found " + search_title + " by " 
               //    + tunes_array[k].getSArtist() );
               break;   // found
            }
         }
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

Doing 5000000 searches in array having 79 iTunes.

Algorithm Elapsed Time: 2.9033 seconds

---------

Doing 500000 searches in array having 79 iTunes.

Algorithm Elapsed Time: 0.3116 seconds.

---------

Doing 50000 searches in array having 79 iTunes.

Algorithm Elapsed Time: 0.0385 seconds.

---------

Doing 5000 searches in array having 79 iTunes.

Algorithm Elapsed Time: 0.0086 seconds.

---------

Doing 500 searches in array having 79 iTunes.

Algorithm Elapsed Time: 0.0019 seconds.

---------------------------------------- */