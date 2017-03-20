package assign2A;
import java.util.ListIterator;

import cs_1c.*; 

public class SparseMat_V2<E>
{
   protected int row_size, col_size;
   protected E default_val;
   protected FHarrayList < FHlinkedList< MatNode > > rows;
   
   SparseMat_V2( int num_rows, int num_cols, E default_v)
   {
      //row and column size >=1 , default value of all elements
      if (num_rows < 1 || num_cols < 1 || default_v == null)
         return;
      
      row_size = num_rows;
      col_size = num_cols;
      default_val = default_v;
      System.out.println("In the constructor");
      
      //call allocateEmptyMatrix
      allocateEmptyMatrix();
   }
   
   void allocateEmptyMatrix(){
      rows = new FHarrayList< FHlinkedList< MatNode > >(row_size);
      
      for (int couter = 0 ; couter < row_size ; couter ++)
      {
         rows.add(couter, new FHlinkedList< MatNode >());
      }
   }
   
   E get(int r, int c){
      //throw out of bound exception if r or c is not valid
      if (r < 0 || r >= row_size || c < 0 || c >= col_size)
         throw new IndexOutOfBoundsException();
      
      E ret_value = default_val;
      
      //if no column member in the row yet
      if (rows.get(r).isEmpty())
         return ret_value;
      
      //if there are column members in the row
      else
      {
         ListIterator< MatNode > iter = null;
         for (iter = rows.get(r).listIterator(); iter.hasNext();  )
         {
            MatNode tmpNode = iter.next();
            //column found get return value and break 
            if( c == tmpNode.getCol() )
            {
               ret_value = tmpNode.data;
               break;
            }
            
            //as the list is sorted break if the provided column is less than 
            //the current linked list node's column
            else if ( tmpNode.getCol() > c )
               break;
         }  
         return ret_value;
      }
   }

   boolean set(int r, int c, E x)
   {
      //if r or c are bad return false
      if (r < 0 || r >= row_size || c < 0 || c >= col_size)
         return false;
      
      MatNode mt = new MatNode(c, x);
      
      //no member in this row yet
      if (rows.get(r).isEmpty())
      {
         //if the value is not default add a new linked list to the row
         if (!x.equals(default_val))
         {
            FHlinkedList< MatNode > newLinkedList = new FHlinkedList< MatNode >();
            newLinkedList.addFirst( mt );
            rows.set( r, newLinkedList );
         }
      }
      
      //row has some members in the list
      else
      {
         boolean done = false;
         ListIterator< MatNode > iter;
         for (iter = rows.get(r).listIterator(); iter.hasNext();  )
         {
            MatNode tmpNode = iter.next();
            
            //if column exists and x is not the default value, 
            //set the new node as current node
            if ( mt.getCol() == tmpNode.getCol() && x != default_val )
            {
               iter.set( mt );
               done = true;
               break;
            }
            
            //if column exists and x is default, remove the column
            else if ( mt.getCol() == tmpNode.getCol() && x == default_val )
            {
               iter.previous();
               iter.remove();
               done = true;
               break;
            }
            
            //column does not exists
            else if ( tmpNode.getCol() > mt.getCol() )
            {
               iter.previous();
               iter.add( mt );
               done = true;
               break;
            }
         }
         //if column is the highest add it at the end of the linked list
         if (!done)
            rows.get(r).addLast( mt );
      }
      return true;
   }

   void clear()
   {
      allocateEmptyMatrix();
      // clears all the rows, effectively setting all values to the default_val 
      //(but leaves the matrix size unchanged)
   }
   
   void showSubSquare(int start, int size)
   {
      int iterations = start + size ;
      
      System.out.println("--------------------------------");
      System.out.print(String.format("%9s", ""));
      for (int col_count = start; col_count < iterations; col_count++ )
      {
         System.out.print(String.format("%-7s", col_count));
      }
      System.out.println("\n--------------------------------");
      
      for (int row_count = start; row_count < iterations; row_count++ )
      {
         System.out.print(String.format("%7s", row_count +" |"));
         for (int col_count = start; col_count < iterations; col_count++ )
         {
            System.out.print(String.format("%7s", get(row_count, col_count) ) );
         }
         System.out.println();
      }
      System.out.println("\n--------------------------------");
   }
   
   
   protected class MatNode
   {
      public int col;
      public E data;
      
      // we need a default constructor for lists
      MatNode()
      {
         col = 0;
         data = null;
      }

      MatNode(int cl, E dt)
      {
         col = cl;
         data = dt;
      }
      
      public int getCol() { return col; }
   };
   
   
   
}