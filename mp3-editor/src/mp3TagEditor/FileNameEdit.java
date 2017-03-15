package mp3TagEditor;

import java.io.File;
import java.util.ArrayList;
import java.util.Iterator;

public class FileNameEdit
{

   public FileNameEdit()
   {
   }

   public static void renameFile(File oldFile, String[] str2rem, String album,
         int track)
   {

      String fileName = oldFile.getName();

      fileName = fileName.replaceAll("(?i)" + ".mp3", "");
      for (int i = 0; i < str2rem.length; i++)
         fileName = fileName.replaceFirst("(?i)" + str2rem[i], "");

      fileName = fileName.replaceAll("[^a-zA-Z\\s]", "");
      fileName = fileName.trim();
      if (fileName.compareTo("") == 0)
      {
         fileName = album + track;
      }
      File newFile = new File(oldFile.getParent() + "/" + fileName + "-"
            + album + ".mp3");
      System.out.println(oldFile.toString() + " --> " + newFile.toString());
      oldFile.renameTo(newFile);
   }

   public static void renameFileAsSong(File oldFile, String album, String song)
   {

      File newFile = new File(oldFile.getParent() + "/" + song + "-" + album
            + ".mp3");

      System.out.println(oldFile.toString() + " --> " + newFile.toString());
      oldFile.renameTo(newFile);

   }
}
