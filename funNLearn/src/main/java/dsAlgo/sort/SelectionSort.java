package dsAlgo.sort;

public class SelectionSort

{
   int arr[] = {2, 7, 6, 4, 1, 8, 5, 3};
  
   public void selectSort()
   {
      /* start from beginning of the array */
      for(int i=0; i < arr.length; i++)
      {
         // for every i go through i+1 to end of array
         for(int j=i+1; j < arr.length; j++)
         {
            // if arr[j] < arr[i] swap elements
            if(arr[j] < arr[i])
            {
               int temp = arr[j];
               arr[j] = arr [i];
               arr[i] = temp;
            }
         }
      }
   }
  
   public static void main(String args[])
   {
      SelectionSort ss = new SelectionSort();
      ss.selectSort();
      for (int i=0; i < ss.arr.length; i++)
         System.out.print(ss.arr[i]+", ");
   }
}