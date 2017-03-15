package dsAlgo;

import java.util.Arrays;
import java.util.Hashtable;
import java.util.LinkedHashSet;
import java.util.Set;

public class MyString
{
   // Using Hashtable, Time: O(n2), Space: O(n) 
   public void removeDuplicates(char [] str)
   {
      Hashtable<Character, Integer> charset = new Hashtable<Character, Integer>();
      int numOfDups = 0;
      for (int i= 0; i < str.length-numOfDups; i++)
      {
         if(charset.containsKey(str[i]))
         {
            numOfDups++;
            int j;
            for ( j = i; j<str.length-numOfDups;j++)
               str[j] = str[j+1];
            str[j]='\0';
            i--;
         }
         else
            charset.put(str[i], 1);
      }
      
      for(int k =0; k<str.length; k++)
         System.out.print(str[k]);
      System.out.println();
   }
   
   // Using LinkedHashSet, Time: O(2n) = O(n), Space: O(n)
   public void removeDuplicates1(char[] str)
   {
      LinkedHashSet<Character> lhs= new LinkedHashSet<Character>();
      for (int i=0; i<str.length; i++)
         lhs.add(str[i]);
      
      StringBuilder sb = new StringBuilder ();
      for (Character c : lhs)
         sb.append(c);
      str = sb.toString().toCharArray();
      
      for(int k =0; k<str.length; k++)
         System.out.print(str[k]);
      System.out.println();
   }
   
   // Substrings superset, Time: O(n2), Space: O(n2)
   public void getSubStrings(String str)
   {
      Set<String> hs = new LinkedHashSet<String>();
      for (int i = 0; i<str.length(); i++)
         for (int j = 1; j<= str.length()-i;j++)
            hs.add(str.substring(i, i+j));
      System.out.println(hs.toString());
   }
   
   // O(n) time using O(n) space
   public String removeChars(String str, char c)
   {
      StringBuilder sb = new StringBuilder();
      int i = 0;
      while (i<str.length())
      {
         if (str.charAt(i)!=c)
            sb.append(str.charAt(i));
         i++;
      }
      return sb.toString();
   }
   
   // O(n2) time no extra space
   public void removeChars(char [] charstr, char c)
   {
      int i = charstr.length-1;
      int count = 0;
      
      while (i>=0)
      {
         if (charstr[i]==c)
         {
            int j = i;
            while (j < charstr.length-1-count)
            {
               charstr[j]=charstr[j+1];
               j++;
               count++;
            }
            charstr[j]='\0';
         }
         else
            i--;
      }
      
      for(int k = 0; k<charstr.length; k++)
         System.out.print(charstr[k]);
      System.out.println();
   }
   
   // O(n) time using O(n) space
   public String replaceChars(String str, char c1, char c2)
   {
      StringBuilder sb = new StringBuilder();
      int i = 0 ;
      while (i<str.length())
      {
         if (str.charAt(i)!=c1)
            sb.append(str.charAt(i));
         else 
            sb.append(c2);
         i++;
      }
      return sb.toString();
   }
   
   // O(n) time no extra space
   public void replaceChars(char [] charstr, char c1, char c2)
   {
      int i = charstr.length-1;
      
      while (i>=0)
      {
         if (charstr[i]==c1)
            charstr[i]=c2;
         i--;
      }
      for(int k = 0; k<charstr.length; k++)
         System.out.print(charstr[k]);
      System.out.println();
   }

   public String reverse(String str)
   {
      StringBuilder sb = new StringBuilder();
      if (str.length()==1)
         return str;
      else 
         sb.append(reverse(str.substring(1))+str.charAt(0));
      
      return sb.toString();
   }
   
   public void reverse(char []str)
   {
      for (int i=0; i < (str.length)/2; i++)
      {
         char temp = str[i];
         str[i]=str[(str.length)-1-i];
         str[(str.length)-1-i] = temp;
      }
   }
   
   public String reverse1(String str)
   {
      StringBuilder sb = new StringBuilder();
      for (int i=str.length()-1; i>=0; i--)
      {
         sb.append(str.charAt(i));
      }
      return sb.toString();
   }
   
   // Time O(n2), no extra space
   public int getSubStrCount(String str, String sub){
      int count=0;
      int i = 0;
      while (i<str.length())
      {
         System.out.println("this is i:"+i);
         int match = 0;
         int j = 0;
         while (j<sub.length() && (i+j) < str.length())
         {
            System.out.println(i+j);
            if (str.charAt(i+j)==sub.charAt(j))
            {
               match++;
               j++;
            }
            else 
               break;
         }
         
         if (match==sub.length())
         {
            count++;
            i=i+sub.length();
         }
         else
            i++;
      }//for int i
      
      return count;
   }
   
   // Time O(n), no extra space
   public int getSubStrCount1(String str,String sub){
      int count = 0;
      int i = 0;
      int j = 0;
      
      while (i<str.length())
      {
         System.out.println("i: "+ i);
         System.out.println("j: "+ j);
         if (j==sub.length())
         {
            count++;
            System.out.println("Incrementing Count : "+ count);
            j=0;
         }
         
         if (str.charAt(i)==sub.charAt(j))
         {
            i++;
            j++;
         }
         else 
         {
            i++;
            j=0;
         }
      }
      return count;
   }
   
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
   
   public static void main(String[] args)
   {
      // Remove Duplicates test cases
      String str1 = "vishal mittalv";
      String str2 = "abababab";
      String str3 = "vishvishvishvish";
      String str4 = "aaaabbbb";
      
      MyString ms = new MyString ();
      ms.removeDuplicates(str1.toCharArray());
      ms.removeDuplicates(str2.toCharArray());
      ms.removeDuplicates(str3.toCharArray());
      ms.removeDuplicates(str4.toCharArray());
      
      ms.removeDuplicates1(str1.toCharArray());
      ms.removeDuplicates1(str2.toCharArray());
      ms.removeDuplicates1(str3.toCharArray());
      ms.removeDuplicates1(str4.toCharArray());
      
      ms.getSubStrings("vishal");
      
      
      
      
   }

}
