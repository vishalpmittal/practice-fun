package dsAlgo.sort;

public class QuickSort
{
   static void quick_srt(int arr[], int left, int right) {
      int index = partition(arr, left, right);
     
      if (left < index - 1)
         quick_srt(arr, left, index - 1);
      if (index < right)
         quick_srt(arr, index, right);
   }
  
   static int partition(int arr[], int left, int right)
   {
         int i = left, j = right;
         int tmp;
         int pivot = arr[(left + right) / 2];
       
         while (i <= j)
         {
               while (arr[i] < pivot)
                     i++;
               while (arr[j] > pivot)
                     j--;
               if (i <= j) {
                     tmp = arr[i];
                     arr[i] = arr[j];
                     arr[j] = tmp;
                     i++;
                     j--;
               }
         };
         return i;
   }
  
   public static void print(int[] myArr)
   {
      for(int i=0; i<myArr.length; i++)
         System.out.print(myArr[i]+ ", ");
      System.out.println();
   } 
  
   public static void main(String a[])
   {
      int array[] = {2, 8, 7, 6, 4, 1, 8, 5, 3, 2, 10};
     
      System.out.println("Values Before the sort:");
      print(array);
     
      quick_srt(array, 0, array.length - 1);
     
      System.out.print("\nValues after the sort:\n");
      print(array);
   }
}