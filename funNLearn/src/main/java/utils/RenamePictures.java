package utils;

import java.io.File;
import java.io.IOException;
import java.text.ParseException;

public class RenamePictures {
    public static String[] getDirContents(String path) {
        String[] contents = null;
        File f = new File(path);
        if (!f.exists() || f.isFile()) {
            return contents;
        }
        return f.list();
    }

    public static void renameFilesUsingParentDir(String path, Boolean changeTimestamp, boolean changeEXIF)
            throws Exception {
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
                renameFilesUsingParentDir(file.getAbsolutePath(), changeTimestamp, changeEXIF);
            } else {
                String ext = file.getName().substring(file.getName().lastIndexOf(".") + 1);
                if (ext.compareTo("db") == 0) {
                    continue;
                }

                if (changeEXIF) {
                    chageEXIFMetadata(date + "101017", file);
                }

                String nName = date + "_" + albumName + "_" + String.format("%04d", counter++) + "." + ext;
                File nFile = new File(file.getParentFile().getAbsolutePath() + File.separator + nName);
                file.renameTo(nFile);

                if (changeTimestamp) {
                    changeTimestampOfFile(date + "1010", nFile);
                }
            }
        }
    }

    public static void chageEXIFMetadata(String yyyyMMddhhmmssDate, File file)
            throws InterruptedException, IOException {
        String exifDate = yyyyMMddhhmmssDate.substring(0, 4) + ":" + yyyyMMddhhmmssDate.substring(4, 6) + ":"
                + yyyyMMddhhmmssDate.substring(6, 8) + " " + yyyyMMddhhmmssDate.substring(8, 10) + ":"
                + yyyyMMddhhmmssDate.substring(10, 12) + ":" + yyyyMMddhhmmssDate.substring(12, 14);

        String cmd = "/usr/local/bin/exiftool" + " -artist=\"Vishal Mittal\"" + " -copyright=\"2017 Vishal Mittal\""
                + " -AllDates=\"" + exifDate + "\"" + " -overwrite_original" + " " + file.getAbsolutePath();

        Runtime.getRuntime().exec(cmd).waitFor();

    }

    public static void changeTimestampOfFile(String yyyyMMddhhmmDate, File f)
            throws ParseException, IOException, InterruptedException {

        String cmd = "touch -t" + yyyyMMddhhmmDate + " " + f.getAbsolutePath();
        Runtime.getRuntime().exec(cmd).waitFor();

        cmd = "touch -mt" + yyyyMMddhhmmDate + " " + f.getAbsolutePath();
        Runtime.getRuntime().exec(cmd).waitFor();

        String setFileDate = yyyyMMddhhmmDate.substring(4, 6) + "/" + yyyyMMddhhmmDate.substring(6, 8) + "/"
                + yyyyMMddhhmmDate.substring(0, 4) + " " + yyyyMMddhhmmDate.substring(8, 10) + ":"
                + yyyyMMddhhmmDate.substring(10, 12);

        cmd = "/usr/bin/SetFile -d \"" + setFileDate + "\" " + f.getAbsolutePath();
        System.out.println(cmd);
        Runtime.getRuntime().exec(cmd).waitFor();

        cmd = "/usr/bin/SetFile -m \"" + setFileDate + "\" " + f.getAbsolutePath();
        Runtime.getRuntime().exec(cmd).waitFor();

    }

    public static void main(String[] args) throws Exception {
        String workDir = "/Users/vishalm/Pictures/work/20170318_TESTHoli";
        renameFilesUsingParentDir(workDir, true, true);
    }

}
