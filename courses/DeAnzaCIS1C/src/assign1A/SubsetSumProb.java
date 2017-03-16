package assign1A;
//CS1C Assignment 1A
//Vishal Mittal

import java.text.NumberFormat;
import java.util.*;

//------------------------------------------------------
public class SubsetSumProb
{
   // -------  main --------------
   public static void main(String[] args) throws Exception
   {
      int TARGET = 72;
      ArrayList<Integer> data_set = new ArrayList<Integer>();
      ArrayList<Sublist> choices = new ArrayList<Sublist>();
      long start_time, end_time;
      int dataSetIndex, subListIndex; 
      int num_sets = 0; 
      int bestSum = 0; 
      int bestSublistIndex = 0;

      // for formatting and timing
      NumberFormat tidy = NumberFormat.getInstance(Locale.US);
      tidy.setMaximumFractionDigits(4);
      
      
      data_set.add(4); data_set.add(12); data_set.add(22);
      data_set.add(5); data_set.add(15); data_set.add(25);
      data_set.add(9); data_set.add(19); data_set.add(29);
      
      // START TIMING THE ALGORITHM
      start_time = System.nanoTime();
      
      //get the first sublist which that has no indices
      Sublist empty_sublist = new Sublist(data_set);
      
      //add the empty sublist to the choices ArrayList
      choices.add(empty_sublist);      
      num_sets=1;
      
      OuterFor: for(dataSetIndex=0; dataSetIndex<data_set.size(); dataSetIndex++)
      {
         //verity that the number itself is not greater than TARGET
         if (data_set.get(dataSetIndex)<=TARGET)
         {
            //get num of sublists
            int choice_size = choices.size();
             
            //for each sublist
            for(subListIndex=0; subListIndex<choice_size; subListIndex++)
            {
               //add integer in data set to each sublist
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
      
      
      System.out.println("Target time: " + TARGET);
      choices.get(bestSublistIndex).showSublist();
      
      // report algorithm time
      System.out.println("\nAlgorithm Elapsed Time: "
         + tidy.format( (end_time - start_time) / 1e9)
         + " seconds.");
   }
}