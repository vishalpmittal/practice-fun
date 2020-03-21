/**
 * Tag: sort
 * 
 */

package dsAlgo.sort;

public class BubbleSort {
   int arr[] = { 2, 7, 6, 4, 1, 8, 5, 3 };

   public void bSort() {
      /* from zeroth element to n-1th element */
      for (int i = 0; i < arr.length - 2; i++) {
         // from 1st to arr.length-1th element compare
         // every adjacent pair and swap if left > right
         for (int j = 1; j < arr.length - i; j++) {
            if (arr[j - 1] > arr[j]) {
               int temp = arr[j - 1];
               arr[j - 1] = arr[j];
               arr[j] = temp;
            }
         }
      }
   }

   public static void main(String args[]) {
      BubbleSort ss = new BubbleSort();
      ss.bSort();
      for (int i = 0; i < ss.arr.length; i++)
         System.out.print(ss.arr[i] + ", ");
   }
}