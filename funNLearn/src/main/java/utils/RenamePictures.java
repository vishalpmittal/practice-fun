package utils;

import java.io.File;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.lang.Runtime;
import java.lang.Process;

public class RenamePictures {
    public static String[] getDirContents(String path) {
        String[] contents = null;
        File f = new File(path);
        if (!f.exists() || f.isFile()) {
            return contents;
        }
        return f.list();
    }

    public static void renameFilesUsingParentDir(String path, Boolean changeTimestamp) throws Exception {
        File parDir = new File(path);

        if (!parDir.exists() || parDir.isFile()) {
            System.out.println("File Does not exists!!!  Exiting");
            return;
        }

        String temp = path.substring(path.lastIndexOf(File.separator) + 1);
        String date = temp.substring(0, temp.indexOf("_"));
        String albumName = temp.substring(temp.indexOf("_") + 1);
        int counter = 1;

        for (File file : parDir.listFiles()) {
            if (file.getName().charAt(0) == '.')
                continue;

            if (file.isDirectory()) {
                System.out.println(file.getAbsolutePath());
                renameFilesUsingParentDir(file.getAbsolutePath(), changeTimestamp);
            } else {
                String ext = file.getName().substring(file.getName().lastIndexOf(".") + 1);
                if (ext.compareTo("db") == 0) {
                    continue;
                }
                String nName = date + "_" + albumName + "_" + String.format("%04d", counter++) + "." + ext;
                File nFile = new File(file.getParentFile().getAbsolutePath() + File.separator + nName);
                file.renameTo(nFile);

                if (changeTimestamp) {
                    changeTimestampOfFile(date + "1011", nFile);
                }
            }
        }
    }

    public static void changeTimestampOfFile(String yyyyMMddhhmmDate, File f)
            throws ParseException, IOException, InterruptedException {
        // SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMddhhmm");
        // Date newDate = sdf.parse(yyyyMMddhhmmDate);
        // f.setLastModified(newDate.getTime());
        Runtime rt = Runtime.getRuntime();

        String cmd = "touch -t" + yyyyMMddhhmmDate + " " + f.getAbsolutePath();
        String cmd1 = "touch -mt" + yyyyMMddhhmmDate + " " + f.getAbsolutePath();
        Process p = rt.exec(cmd);
        p.waitFor();

        p = rt.exec(cmd1);
        p.waitFor();
    }

    public static void main(String[] args) throws Exception {
        String workDir = "/Users/vishalm/Pictures/work/20060101_ToDo";
        renameFilesUsingParentDir(workDir, true);
    }

}
