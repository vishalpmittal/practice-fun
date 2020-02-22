package dsAlgo.others;

public class isPrimeCheck
{
   public static boolean isPrime (int n)
   {
       int divisor = 2;
       while ( divisor < n )
        { 
              if ( n % divisor == 0 )
                   return false;
              else
                    divisor++;
        }
         return true;
   }
}
