package exercises;

//Sample main() for creating an ordered list of iTunesEntry objects
//CS 1C, Foothill College, Michael Loceff, creator

import java.util.*;
import cs_1c.*;

//------------------------------------------------------
public class OrderedVsRegItunesList
{
   // ------- main --------------
   public static void main(String[] args) throws Exception
   {
      // read the data from file
      iTunesEntryReader tunes_input = new iTunesEntryReader("itunes_file.txt");
      int array_size, k;
      FHlinkedList<iTunesEntry> tunes_list = new FHlinkedList<iTunesEntry>();
      Iterator<iTunesEntry> iter;

      // test the success of the read
      if (tunes_input.readError())
      {
         System.out.println("couldn't open " + tunes_input.getFileName()
               + " for input.");
         return;
      }
      array_size = tunes_input.getNumTunes();

      // prepare to insert into the list by the time, from shortest to longest
      iTunesEntry.setNSortType(iTunesEntry.SORT_BY_TIME);

      // prepare to build a list of iTunes
      for (k = 0; k < array_size; k++)
         tunes_list.addLast(tunes_input.getTune(k));

      System.out.println("\n---------- out-of-order list ----------------");
      for (iter = tunes_list.iterator(); iter.hasNext();)
         System.out.print(iter.next().convertTimeToString() + "  ");
      System.out.println();

      // repeat, this time inserting in sorted order
      tunes_list.clear();
      for (k = 0; k < array_size; k++)
         insertInOrder(tunes_list, tunes_input.getTune(k));

      System.out.println("\n---------- ordered list ----------------");
      for (iter = tunes_list.iterator(); iter.hasNext();)
         System.out.print(iter.next().convertTimeToString() + "  ");
      System.out.println();
   }

   static void insertInOrder(FHlinkedList<iTunesEntry> the_list,
         iTunesEntry the_tune)
   {
      ListIterator<iTunesEntry> iter;

      for (iter = the_list.listIterator(); iter.hasNext();)
         if (the_tune.compareTo(iter.next()) < 0)
         {
            iter.previous(); // back up one - we just passed the spot
            break;
         }

      // regardless of how we ended loop, we are at the correct position)
      iter.add(the_tune);
   }

   // static void insertInOrder() shown above
}

/*
 * ---------------------------------- Run ----------------------------------
 * 
 * ---------- out-of-order list ---------------- 3:56 3:40 3:48 4:23 3:50 4:43
 * 5:08 2:58 2:55 3:36 3:14 3:28 7:23 3: 50 4:36 3:07 3:02 5:43 4:17 3:21 3:12
 * 3:04 1:09 13:59 13:20 2:21 2: 34 2:55 2:48 3:24 4:58 4:30 1:19 2:35 5:48 4:55
 * 3:59 3:24 3:48 3:38 4:03 4:36 3:37 3:15 3:30 5:56 4:59 4:12 2:27 7:14 7:25
 * 6:42 3:06 2:57 7:42 4:16 3:24 3:12 6:07 12:22 5:11 3:27 5:10 4:38 5:51 7:31 5
 * :25 15:41 5:13 3:51 3:55 3:47 5:31 2:51 3:31 4:20 3:20 5:47 3:50
 * 
 * ---------- ordered list ---------------- 1:09 1:19 2:21 2:27 2:34 2:35 2:48
 * 2:51 2:55 2:55 2:57 2:58 3:02 3: 04 3:06 3:07 3:12 3:12 3:14 3:15 3:20 3:21
 * 3:24 3:24 3:24 3:27 3:28 3:30 3:31 3:36 3:37 3:38 3:40 3:47 3:48 3:48 3:50
 * 3:50 3:50 3:51 3:55 3:56 3:59 4:03 4:12 4:16 4:17 4:20 4:23 4:30 4:36 4:36
 * 4:38 4: 43 4:55 4:58 4:59 5:08 5:10 5:11 5:13 5:25 5:31 5:43 5:47 5:48 5:51
 * 5:56 6:07 6:42 7:14 7:23 7:25 7:31 7:42 12:22 13:20 13:59 15:41
 * 
 * ---------------------------------------------------------------------------
 */