package exercises;

//generic FHstack class ------------------------------------
//(shown above)

public class FHStackTest
{
public static void main (String[] args) throws CloneNotSupportedException
{
   int k;

   FHstack<Integer> my_stack = new FHstack<Integer>();

   for (k = 0; k < 10; k++)
      my_stack.push(k);

   int the_top = my_stack.top();
   System.out.println("top: " + the_top );

   for (k = 0; k < 12; k++)
      System.out.println( my_stack.pop() );
}
}