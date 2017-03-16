//CS1C Assignment 1C
//Vishal Mittal

package assign1B;

import cs_1c.*;
import java.text.*;
import java.util.*;

//------------------------------------------------------
public class SubsetSumITunesEntry
{
   // -------  main --------------
   public static void main(String[] args) throws Exception
   {
      int TARGET = 3600;
      ArrayList<iTunesEntry> data_set = new ArrayList<iTunesEntry>();
      ArrayList<Sublist> choices = new ArrayList<Sublist>();
      long start_time, end_time;
      int k, array_size;
      int dataSetIndex, subListIndex; 
      int num_sets = 0; 
      int bestSum = 0; 
      int bestSublistIndex = 0;
      
      // for formatting and timing
      NumberFormat tidy = NumberFormat.getInstance(Locale.US);
      tidy.setMaximumFractionDigits(4);
      
      // read the iTunes Data
      iTunesEntryReader tunes_input = new iTunesEntryReader("itunes_file.txt");

      // test the success of the read:
      if (tunes_input.readError())
      {
         System.out.println("couldn't open " + tunes_input.getFileName()
            + " for input.");
         return;
      }

      // load the data_set ArrayList with the iTunes:
      array_size = tunes_input.getNumTunes();
      for (k = 0; k < array_size; k++)
         data_set.add(tunes_input.getTune(k));

      choices.clear();
      System.out.println("Target time: " + TARGET);
      
      // START TIMING THE ALGORITHM
      start_time = System.nanoTime();
      
      choices.add( new Sublist( data_set ) ); // this represents the 0 set
      num_sets=1;
      
      OuterFor: for(dataSetIndex=0; dataSetIndex<data_set.size(); dataSetIndex++)
      {
         //verify that the time itself is not greater than TARGET
         if (data_set.get(dataSetIndex).getNTime()<=TARGET)
         {
            //get num of sublists
            int choice_size = choices.size();
             
            //for each sublist
            for(subListIndex=0; subListIndex<choice_size; subListIndex++)
            {
               //add add tune in data set to each sublist
               Sublist new_sublist = choices.get(subListIndex).
                       addItem(dataSetIndex);
               
               //if sum is exactly equal to TARGET
               if (new_sublist.getSum() == TARGET)
               {
                  choices.add(new_sublist);
                  bestSublistIndex = num_sets;
                  num_sets += 1;
                  break OuterFor;
               }
               
               //if sum is less than target save the best sum 
               //and the index of best sum sublist
               else if (new_sublist.getSum() < TARGET)
               {
                  choices.add(new_sublist);
                  if (new_sublist.getSum() > bestSum)
                     bestSublistIndex = num_sets;
                  num_sets += 1;
               }
            }
         } // end of if num > TARGET
      }  //end of OuterFor loop
            
      // END TIMING
      end_time = System.nanoTime();
      
      choices.get(bestSublistIndex).showSublist();

      // report algorithm time
      System.out.println("\nAlgorithm Elapsed Time: "
         + tidy.format( (end_time - start_time) / 1e9)
         + " seconds.");
      
   }
}