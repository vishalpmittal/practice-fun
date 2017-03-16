package assign2A;

//client -----------------------------------------------------
import cs_1c.*;

//------------------------------------------------------
public class SparseMatTest
{
   final static int MAT_SIZE = 100000;

   // ------- main --------------
   @SuppressWarnings("unchecked")
   public static void main(String[] args) throws Exception
   {
      // 100000 x 100000 filled with 0
      SparseMat mat = new SparseMat(MAT_SIZE, MAT_SIZE, 0.0);

      for (int i = 0; i < 10; i++)
         for (int j = 0; j < 10; j++)
            mat.set(i, j, Double.parseDouble(i + "." + j));

      for (int i = 0; i < 5; i++)
         mat.set(i, i, 0.0);

      for (int i = 5; i < 10; i++)
         mat.set(i, i, i);

      // test mutators
      mat.set(2, 5, 10.0);
      mat.set(2, 5, 35.0); // should overwrite the 10
      mat.set(3, 9, 21.0);
      mat.set(100000, 1, 5.0); // should fail silently
      mat.set(9, 9, mat.get(3, 9)); // should copy the 21 here
      mat.set(4, 4, -9.0);
      mat.set(4, 4, 0.0); // should remove the -9 node entirely
      mat.set(MAT_SIZE - 1, MAT_SIZE - 1, 99.0);

      // test accessors and exceptions
      try
      {
         System.out.println(mat.get(7, 8));
         System.out.println(mat.get(2, 5));
         System.out.println(mat.get(9, 9));
         System.out.println(mat.get(0, 0));
         System.out.println(mat.get(-4, 7)); // should throw an exception
      } catch (IndexOutOfBoundsException e)
      {
         System.out.println("oops!!! Caught IndexOutOfBoundException");
      }

      // show top left 15x15
      mat.showSubSquare(0, 15);

      // show bottom right 15x15
      mat.showSubSquare(MAT_SIZE - 15, 15);

      mat.clear();
      System.out.println("Matrix after clearing up-> ");
      mat.showSubSquare(0, 10);
      mat.showSubSquare(MAT_SIZE - 10, 10);
   }
}