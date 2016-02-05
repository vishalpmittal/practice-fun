package problems;

import java.io.File;
import java.util.PriorityQueue;
import java.util.Queue;

public class BreadthFirstDepthFirstListing
{
   Queue <File> fileQueue = new PriorityQueue<File>();
   
   public void depthFirstListing(String path, File file)
   {
      File absFile = new File(path+file.getName());
      
      if (absFile.isFile())
      {   
         System.out.println("1   |-> "+file.getName());
         return;
      }
      
      String [] temp = absFile.list();
      
      for(String tempName : temp)
      {
         File tempFile = new File(tempName);
         
         if ((new File(path+absFile.getName()+"/"+tempFile)).isFile())
            System.out.println("   |-> "+tempFile.getName());
         
         else if((new File(path+absFile.getName()+"/"+tempFile)).isDirectory())
         {
            System.out.println("|-> "+tempFile.getName());
            depthFirstListing(path+file.getName()+"/", tempFile);
         }
      }
   }
   
   public void depthFirstListing(File file)
   {
      if (file.isFile())
      {   
         System.out.println("1   |-> "+file.getName());
         return;
      }
      
      String [] temp = file.list();
      
      for(String tempName : temp)
      {
         File tempFile = new File(tempName);
         
         if ((new File(file.getAbsolutePath()+"/"+tempFile)).isFile())
            System.out.println("   |-> "+tempFile.getName());
         
         else if((new File(file.getAbsolutePath()+"/"+tempFile)).isDirectory())
         {
            System.out.println("|-> "+tempFile.getName());
            depthFirstListing((new File(file.getAbsolutePath()+"/"+tempFile)));
         }
      }
   }

   public void breadthFirstListing(File file)
   {
      if (file== null)
         return;
      
      fileQueue.add(file);
      
      while(!fileQueue.isEmpty())
      {
         File tempFile = fileQueue.poll();
         System.out.println(tempFile.getName());
         if (tempFile.isDirectory())
         {
            String[] fileList = tempFile.list();
            
            for (String temp : fileList)
            {
               System.out.println("Adding: "+tempFile.getAbsolutePath()+"/"+temp);
               fileQueue.add(new File(tempFile.getAbsolutePath()+"/"+temp));
            }
            
         } //if directory
         
      } //while
   }
   
   public static void main(String[] args)
   {
      String path = "/Users/vishalmittal/Music/";
      File listDir = new File("Gazals");
      File dir = new File("/Users/vishalmittal/Music/HindiMovieSongs/2013/");
      BreadthFirstDepthFirstListing mf = new BreadthFirstDepthFirstListing();
      
      //mf.depthFirstListing(path, listDir);
      //mf.depthFirstListing(dir);
      mf.breadthFirstListing(dir);
   }

}
