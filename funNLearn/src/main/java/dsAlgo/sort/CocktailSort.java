package dsAlgo.sort;

public class CocktailSort
{
   int arr[] = {2, 7, 6, 4, 1, 8, 5, 3};

   public void bSort()
   {
      // variable to look if no swaps so break
      int swap=0;
      
      for(int i=0; i < arr.length-2; i++)
      {
         swap=0;
         for(int j=i; j <= arr.length-i-2 ; j++)
         {
            if(arr[j]>arr[j+1])
            {
               int temp = arr[j+1];
               arr[j+1] = arr[j];
               arr[j] = temp;
               swap++;
            }
         }
         
         for(int k=arr.length-i-2; k>=i+1; k--)
         {
            if (arr[k]<arr[k-1])
            {
               int temp = arr[k];
               arr[k] = arr[k-1];
               arr[k-1] = temp;
               swap++;
            }
         }
         if (swap==0)
            break;
      }
   }
  
   public static void main(String args[])
   {
      CocktailSort cts = new CocktailSort();
      cts.bSort();
      for (int i=0; i < cts.arr.length; i++)
         System.out.print(cts.arr[i]+", ");
   }
}