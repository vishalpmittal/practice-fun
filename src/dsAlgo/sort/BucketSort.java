package dsAlgo.sort;// Assumption : numbers to be sorted are in the range 0-9

public class BucketSort
{
   // Utility method to print array
   public static void print(int[] myArr)
   {
      for(int i=0; i<myArr.length; i++)
         System.out.print(myArr[i]+ ", ");
      System.out.println();
   }
   
   
   public static void sort(int[] a, int maxVal)
   {
      // create a bucket array of length =9+1 =10
      //i.e. once bucket for each number in our range
      int[] bucket = new int[maxVal + 1];

      // all the buckets have 0 values in it
      for (int i = 0; i < bucket.length; i++)
      {
         bucket[i] = 0;
      }

      // for each number in array to be sorted
      // increment that number's bucket count
      // eg; for any a[i]=2 increment bucket[2]
      for (int i = 0; i < a.length; i++)
      {
         bucket[a[i]]++;
      }
      
      BucketSort.print(bucket);

      // assign sorted values to initial array
      int outPos = 0;
      // for each bucket
      for (int i = 0; i < bucket.length; i++)
      {
         // for count in the bucket
         for (int j = 0; j < bucket[i]; j++)
         {
            //put the bucket number in original array
            a[outPos++] = i;
         }
      }
   }

   public static void main(String[] args)
   {
      int maxVal = 9;
      int[] data =
      { 2, 6, 2, 1, 8, 5, 8, 3, 2, 9, 8, 9 };
      BucketSort.print(data);
      sort(data, maxVal);
      BucketSort.print(data);
   }
}
