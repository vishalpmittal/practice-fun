package utils;

import java.io.File;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class RenamePictures {
    public static String[] getDirContents(String path) {
        String[] contents = null;
        File f = new File(path);
        if (!f.exists() || f.isFile()) {
            return contents;
        }

        return f.list();
    }

    public static Map<String, String> getFileNamesToExtMap(String parentDir){
        
        
        return null;
    }
    
    
    public List<String> getAllDirsInside(String parentDir) {

        return null;
    }

    public List<String> getAllFilesInside(String parentDir) {

        return null;
    }

    public void renameFile(String oldName, String newName) {

    }

    public void changeTimestampOfFile() {

    }

    public static void main(String[] args) {
        String workDir = "/Users/vishalm/Pictures/work/20150502_Ankit_Tiwari_Concert";

        String temp = workDir.substring(workDir.lastIndexOf("/") + 1);
        String date = temp.substring(0, temp.indexOf("_"));
        String albumName = temp.substring(temp.indexOf("_") + 1);
        

        System.out.println(date);
        System.out.println(albumName);
        System.out.println(Arrays.toString(getDirContents(workDir)));

    }

}
