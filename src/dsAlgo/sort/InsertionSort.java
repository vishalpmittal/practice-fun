package dsAlgo.sort;

public class InsertionSort
{
   int arr[] =
   { 2, 7, 6, 4, 1, 8, 5, 3 };

   public void printArr()
   {
      for (int k = 0; k < arr.length; k++)
         System.out.print(arr[k] + ", ");
      System.out.println();
   }

   public void bSort()
   {
      int j; // the number of items sorted so far
      int key; // the item to be inserted
      int i;

      for (j = 1; j < arr.length; j++) // Start with 1 (not 0)
      {
         key = arr[j];
         for (i = j - 1; (i >= 0) && (key < arr[i]); i--) 
         {
            arr[i + 1] = arr[i];
         }
         arr[i + 1] = key; // Put the key in its proper location
      }
   }

   public static void main(String args[])
   {
      InsertionSort cts = new InsertionSort();
      cts.bSort();
      cts.printArr();
   }
}