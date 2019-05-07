package mp3TagEditor;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Properties;

public class MP3Editor {

    File movie_dir;
    public static String[] str2rem;
    String album;
    String comment;
    String genre;
    int year;
    String FILENAME_AS_SONG = "false";

    ArrayList<File> mp3_files;

    // constructor
    public MP3Editor(File property) {
        // read the configuration properties file.
        Properties props = new Properties();
        try {
            FileInputStream propsData = new FileInputStream(property);
            props.load(propsData);
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Get each property from the properties file to local variables
        this.movie_dir = new File((String) props.get("path") + "/" + (String) props.getProperty("movie"));
        str2rem = props.getProperty("text1").split(",");
        this.album = props.getProperty("album");
        this.comment = props.getProperty("comment");
        this.genre = props.getProperty("genre");
        this.year = Integer.parseInt(props.getProperty("year"));
        this.FILENAME_AS_SONG = props.getProperty("replace_file_name_by_album_tag");
        TagEdit.TITLE_TAG_AS_FILENAME = props.getProperty("replace_title_tag_as_filename");

        // get the mp3 file list in the arraylist
        mp3_files = new ArrayList<File>();

        System.out.println(movie_dir.getAbsolutePath());
        for (File fileEntry : movie_dir.listFiles()) {
            if (fileEntry.getName().contains(".mp3"))
                this.mp3_files.add(fileEntry);
        }
    }

    public static void main(String[] args) {

        // command line argument to find properties file

        File prop_file = new File(args[0]);
        System.out.println(prop_file.getAbsolutePath());
        MP3Editor mp3edit = new MP3Editor(prop_file);

        Iterator<File> it = mp3edit.mp3_files.iterator();
        int trackNum = 1;

        while (it.hasNext()) {
            File tmpFile = it.next();

            TagEdit te = new TagEdit(tmpFile);
            String song = te.getTags(mp3edit.album, mp3edit.comment, mp3edit.genre, trackNum, mp3edit.mp3_files.size(),
                    mp3edit.year);

            if (mp3edit.FILENAME_AS_SONG.compareTo("true") == 0)
                FileNameEdit.renameFileAsSong(tmpFile, mp3edit.album, song);
            else
                FileNameEdit.renameFile(tmpFile, MP3Editor.str2rem, mp3edit.album, trackNum);
            trackNum++;

        }
    }
}
