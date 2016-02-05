package problems;

import java.util.Arrays;

public class AnagramCheck
{
   // Using sorting
   public boolean isAnagram(String str1, String str2)
   {
      if (str1.length() == str2.length())
      {
         char [] chr1 = str1.toCharArray();
         Arrays.sort(chr1);
         str1 = new String(chr1);
         
         char [] chr2 = str2.toCharArray();
         Arrays.sort(chr2);
         str2 = new String(chr2);
         
         if (str1.compareTo(str2)==0)
            return true;
         else
            return false;
      }
         
      else
         return false;
   }

   // Using Char set
   public boolean isAnagram1(String str1, String str2)
   {
      int charset[] = new int[256];
      
      if (str1.length()!=str2.length())
         return false;
      
      for (int i=0; i<str1.length(); i++)
         charset[str1.charAt(i)]++;
      
      for (int j=0; j<str2.length(); j++)
      {
         charset[str2.charAt(j)]--;
         if (charset[str2.charAt(j)]<0)
            return false;
      }
      
      for (int k=0; k<256; k++)
      {
         if(charset[k]!=0)
            return false;
      }
      return true;
   }
   
   public static void main (String args[])
   {
      AnagramCheck a = new AnagramCheck();
      System.out.println("Sort isAnagram vishal & lashiv: "+a.isAnagram("vishal", "lashiv"));
      System.out.println("Sort isAnagram vishal & lashiv: "+a.isAnagram("vishal", "lashiv1"));
      
      System.out.println("CharSet isAnagram vishal & lashiv: "+a.isAnagram1("vishal", "lashiv"));
      System.out.println("CharSet isAnagram vishal & lashiv: "+a.isAnagram1("vishal", "lashiv1"));
   }
   
   
}
