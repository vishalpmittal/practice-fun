//CS1C Assignment 1B
//Vishal Mittal

package assign1B;
import java.util.ArrayList;

import cs_1c.iTunesEntry;

class Sublist implements Cloneable
{
   private int sum = 0;
   private ArrayList<iTunesEntry> original_objects;
   private ArrayList<Integer> indices;
   
   // constructor creates an empty Sublist (no indices)
   public Sublist(ArrayList<iTunesEntry> data_set) 
   {
      sum = 0;
      original_objects = data_set;
      indices = new ArrayList<Integer>();
   }
   
   int getSum() { return sum; }
   
   // I have done the clone() for you, since you will need clone() inside addItem().
   @SuppressWarnings("unchecked")
   public Object clone() throws CloneNotSupportedException
   {
      // shallow copy
      Sublist new_object = (Sublist)super.clone();
      // deep copy
      new_object.indices = (ArrayList<Integer>)indices.clone();
      
      return new_object;
   }
   
   Sublist addItem(int index_of_item_to_add )
   {
      //create new sublist object and initialize as null
      Sublist newSublist = null;
      
      try
      {
         //clone the calling sublist
         newSublist = (Sublist) this.clone();
         
         //add the new index to newSublist
         newSublist.indices.add(index_of_item_to_add);         
         
         //update the sum of the newSublist
         newSublist.sum = this.sum + newSublist.
               original_objects.get(index_of_item_to_add).getNTime();
         
      } catch (CloneNotSupportedException e)
      {
         e.printStackTrace();
      }
      return newSublist;
   }
   
   void showSublist()
   {
      System.out.println("Sublist -----------------------------");
      System.out.println("  sum: "+this.sum);
      int sublist_size = this.indices.size();
      if (sublist_size==0)
      {
         System.out.println("  Null Set: {}");
      }
      else
      {
         for (int i=0; i<sublist_size; i++)
         {
            System.out.println("  array["+ indices.get(i)
                  +"] = "+ original_objects.get(indices.get(i))+",");
         }
      }
   }
   
};