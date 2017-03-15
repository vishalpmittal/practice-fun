package mp3TagEditor;

import java.io.File;

import org.blinkenlights.jid3.ID3Exception;
import org.blinkenlights.jid3.ID3Tag;
import org.blinkenlights.jid3.MediaFile;
import org.blinkenlights.jid3.MP3File;
import org.blinkenlights.jid3.v1.ID3V1_0Tag;
import org.blinkenlights.jid3.v2.*;

public class TagEdit
{

   // media file and the tags array
   private MediaFile oMediaFile;
   File file_on_disk;
   ID3Tag[] aoID3Tag;
   static String TITLE_TAG_AS_FILENAME="false";
   
   // constructor gets the tags in an array
   public TagEdit(File file)
   {
      oMediaFile = new MP3File(file);
      file_on_disk = file;
      try
      {
         aoID3Tag = oMediaFile.getTags();
      } catch (ID3Exception e)
      {
         System.out.println("Can not get tags exceptions ... \n"
               + "Problem while getting the tags from the mp3 file.");
         e.printStackTrace();
         System.exit(-1);
      }
   }

   public String getTags(String album, String comment, String genre, int track,
         int ttracks, int year)
   {
      String returnTitle = file_on_disk.getName().replaceAll(".mp3", "");;
      if (aoID3Tag.equals(null) || aoID3Tag.length == 0)
      {
         System.out.println("No tags in the media file. Adding custom V2 tags");
         ID3V2_3_0Tag v2tag = new ID3V2_3_0Tag();

         try
         {
            String tempTitle = file_on_disk.getName().replaceAll(".mp3", "");
            // remove all the unwanted data from the title
            for (int c = 0; c < MP3Editor.str2rem.length; c++)
               tempTitle = tempTitle.replaceAll("(?i)"
                     + MP3Editor.str2rem[c], "");

            // remove all speacial characters and numbers from title
            tempTitle = tempTitle.replaceAll("[^a-zA-Z\\s]", "");

            // trim title
            tempTitle = tempTitle.trim();
            if (tempTitle.compareTo("") == 0
                  || tempTitle.compareTo(" ") == 0)
            {
               tempTitle = track + album;
            }
            
            v2tag.setTitle(tempTitle);
            v2tag.setArtist("VM");
            v2tag.setAlbum(album);
            v2tag.setComment(album + " by VM");
            v2tag.setGenre(genre);
            v2tag.setTrackNumber(track, ttracks);
            v2tag.setYear(year);
            v2tag.setTCOMTextInformationFrame(new TCOMTextInformationID3V2Frame(
                  "Composed by VM"));
            v2tag.setTPE2TextInformationFrame(new TPE2TextInformationID3V2Frame(
                  album + " by VM"));
            v2tag.setTPE3TextInformationFrame(new TPE3TextInformationID3V2Frame(
                  "Band By VM"));
            v2tag.setTPE4TextInformationFrame(new TPE4TextInformationID3V2Frame(
                  "Remixed by VM"));
            v2tag.setTIT1TextInformationFrame(new TIT1TextInformationID3V2Frame(
                  "VM Groups"));
            v2tag.setTIT3TextInformationFrame(new TIT3TextInformationID3V2Frame(
                  tempTitle));
            v2tag.setTEXTTextInformationFrame(new TEXTTextInformationID3V2Frame(
                  "Lyrics by VM"));
            v2tag.setTOLYTextInformationFrame(new TOLYTextInformationID3V2Frame(
                  "Lyrics by VM"));
            oMediaFile.setID3Tag(v2tag);
            oMediaFile.sync();
            returnTitle = tempTitle;
         } catch (ID3Exception e)
         {
            e.printStackTrace();
         }

      } else
      {
         String tempTitle = "";
         for (int i = 0; i < aoID3Tag.length; i++)
         {

            // check to see if we read a v1.0 tag, or a v2.3.0 tag (just for
            // example..)
            if (aoID3Tag[i] instanceof ID3V1_0Tag)
            {
               System.out.println("Editing V1 tags of the media file");
               ID3V1_0Tag v1tag = (ID3V1_0Tag) aoID3Tag[i];

               // -------------------------------------------------------------
               try
               {
                  // ------------title manipulation---------
                  // get the title from the tags
                  tempTitle = v1tag.getTitle();
                  if (tempTitle == null || tempTitle.compareTo("") == 0
                        || tempTitle.compareTo(" ") == 0)
                  {
                     tempTitle = file_on_disk.getName().replaceAll(".mp3", "");
                  }
                  
                  if (TITLE_TAG_AS_FILENAME.compareTo("true") == 0)
                  {
                     tempTitle = file_on_disk.getName().replaceAll(".mp3", "");
                  }

                  // remove all the unwanted data from the title
                  for (int c = 0; c < MP3Editor.str2rem.length; c++)
                     tempTitle = tempTitle.replaceAll("(?i)"
                           + MP3Editor.str2rem[c], "");

                  // remove all speacial characters and numbers from title
                  tempTitle = tempTitle.replaceAll("[^a-zA-Z\\s]", "");

                  // trim title
                  tempTitle = tempTitle.trim();
                  if (tempTitle.compareTo("") == 0
                        || tempTitle.compareTo(" ") == 0)
                  {
                     tempTitle = track + album;
                  }

                  // set the new title to the tag object
                  v1tag.setTitle(tempTitle + "-" + album);

                  // ------------title manipulation---------

                  // ------------Artist manipulation---------
                  // manipulate artist name
                  String tempArtist = v1tag.getArtist();
                  if (tempArtist == null || tempArtist == ""
                        || tempArtist == " ")
                     tempArtist = album + "by VM";

                  for (int c = 0; c < MP3Editor.str2rem.length; c++)
                     tempArtist = tempArtist.replaceAll("(?i)"
                           + MP3Editor.str2rem[c], "");

                  // remove all speacial characters and numbers
                  tempArtist = tempArtist.replaceAll("[^a-zA-Z\\s]", "");

                  // trim artist
                  tempArtist = tempArtist.trim();
                  if (tempArtist.compareTo("") == 0
                        || tempArtist.compareTo(" ") == 0)
                  {
                     tempArtist = album + "by VM";
                  }
                  v1tag.setArtist(tempArtist);
                  // ------------Artist manipulation---------

                  // set the album name to the tag object
                  v1tag.setAlbum(album);

                  // set the Comments to the tag object
                  v1tag.setComment(album + " by VM");

                  oMediaFile.setID3Tag(v1tag);
                  oMediaFile.sync();

               } catch (ID3Exception e)
               {
                  System.out.println("Could get read year from tag: "
                        + e.toString());
               }
            }

            else if (aoID3Tag[i] instanceof ID3V2_3_0Tag)
            {
               System.out.println("Editing V1 tags of the media file");
               ID3V2_3_0Tag oID3V2_3_0Tag = (ID3V2_3_0Tag) aoID3Tag[i];

               try
               {
                  // ---------title manipulation--------------
                  // get the title from the tags
                  tempTitle = oID3V2_3_0Tag.getTitle();
                  if (tempTitle == null || tempTitle.compareTo("") == 0
                        || tempTitle.compareTo(" ") == 0)
                  {
                     tempTitle = file_on_disk.getName().replaceAll(".mp3", "");
                  }
                  
                  if (TITLE_TAG_AS_FILENAME.compareTo("true") == 0)
                  {
                     tempTitle = file_on_disk.getName().replaceAll(".mp3", "");
                  }

                  // remove all the unwanted data from the title
                  for (int c = 0; c < MP3Editor.str2rem.length; c++)
                     tempTitle = tempTitle.replaceAll("(?i)"
                           + MP3Editor.str2rem[c], "");

                  // remove all speacial characters and numbers from title
                  tempTitle = tempTitle.replaceAll("[^a-zA-Z\\s]", "");

                  // trim title
                  tempTitle = tempTitle.trim();
                  if (tempTitle.compareTo("") == 0
                        || tempTitle.compareTo(" ") == 0)
                  {
                     tempTitle = track + album;
                  }

                  // set the new title to the tag object
                  oID3V2_3_0Tag.setTitle(tempTitle + "-" + album);
                  returnTitle = tempTitle;
                  // ---------title manipulation--------------

                  // ---------artist manipulation--------------
                  // manipulate artist name
                  String tempArtist = oID3V2_3_0Tag.getArtist();
                  if (tempArtist == null || tempArtist.compareTo("") == 0
                        || tempArtist.compareTo(" ") == 0)
                  {
                     tempArtist = album + " by VM";
                  }
                  for (int c = 0; c < MP3Editor.str2rem.length; c++)
                     tempArtist = tempArtist.replaceAll("(?i)"
                           + MP3Editor.str2rem[c], "");

                  // remove all speacial characters and numbers
                  tempArtist = tempArtist.replaceAll("[^a-zA-Z\\s]", "");

                  // trim artist
                  tempArtist = tempArtist.trim();
                  if (tempArtist.compareTo("") == 0
                        || tempArtist.compareTo(" ") == 0)
                  {
                     tempArtist = album + " by VM";
                  }
                  oID3V2_3_0Tag.setArtist(tempArtist);
                  // ---------artist manipulation--------------

                  // set the album name to the tag object
                  oID3V2_3_0Tag.setAlbum(album);

                  // set the Comments to the tag object
                  oID3V2_3_0Tag.setComment(album + " by VM");

                  // set the genre to the tag object
                  oID3V2_3_0Tag.setGenre(genre);

                  // set the track number (trackNum of total tracks)
                  oID3V2_3_0Tag.setTrackNumber(track, ttracks);

                  // set the year to the tag object
                  oID3V2_3_0Tag.setYear(year);

                  // update other misc. properties
                  oID3V2_3_0Tag
                        .setTCOMTextInformationFrame(new TCOMTextInformationID3V2Frame(
                              "Composed by VM"));
                  oID3V2_3_0Tag
                        .setTPE2TextInformationFrame(new TPE2TextInformationID3V2Frame(
                              album + " by VM"));
                  oID3V2_3_0Tag
                        .setTPE3TextInformationFrame(new TPE3TextInformationID3V2Frame(
                              "Band By VM"));
                  oID3V2_3_0Tag
                        .setTPE4TextInformationFrame(new TPE4TextInformationID3V2Frame(
                              "Remixed by VM"));
                  oID3V2_3_0Tag
                        .setTIT1TextInformationFrame(new TIT1TextInformationID3V2Frame(
                              "VM Groups"));
                  oID3V2_3_0Tag
                        .setTIT3TextInformationFrame(new TIT3TextInformationID3V2Frame(
                              tempTitle));
                  oID3V2_3_0Tag
                        .setTEXTTextInformationFrame(new TEXTTextInformationID3V2Frame(
                              "Lyrics by VM"));
                  oID3V2_3_0Tag
                        .setTOLYTextInformationFrame(new TOLYTextInformationID3V2Frame(
                              "Lyrics by VM"));

                  oMediaFile.setID3Tag(oID3V2_3_0Tag);
                  oMediaFile.sync();

               } catch (ID3Exception e)
               {
                  System.out.println("Could get read year from tag: "
                        + e.toString());
               }
            }
         }

      }
      return returnTitle;
   }
}