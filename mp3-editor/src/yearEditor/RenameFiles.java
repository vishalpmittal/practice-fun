package yearEditor;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class RenameFiles {
	private static String year="2018";
	private static String replace_title_tag_as_filename="false";
	private static String replace_file_name_by_album_tag="false";
	private static String[] str2rem = {"www.Songs.PK","songs","pk","Songs.PK","www","320Kbps","320kbps","128Kbps",
		"128Kbps","Bollymucom","Bollym4u.com","2004","2005","2007","2008","2009","2010","2011","2012", "2013","mp3pk.com",
		"Muskurahat","Dot","Com", "Songs", "Hindi"};
	
	public static void main (String args[]){
		String prop_file = "/Users/vishalm/Downloads/editor.properties";
		
//		File dir = new File("/Users/vishalmittal/Music/HindiMovieSongs/"+year);
		File dir = new File("/Users/vishalm/Downloads/"+year);
		
		for (final File fileEntry : dir.listFiles()) {
	    	if (fileEntry.isDirectory()){
	    		File oldFile = new File(dir+"/"+fileEntry.getName());
	    		
	    		String newName = fileEntry.getName();
	    		for(int i=0; i<str2rem.length; i++)
	    			newName =newName.replaceAll(str2rem[i], "");
	    		newName = newName.replaceAll(year, "");
	    		newName = newName.replaceAll("[^a-zA-Z\\d\\s]", " ");
	    		newName = newName.trim();
	   
	    		File newFile = new File (dir+"/"+newName+"-"+year);
	    		
	    		System.out.println(oldFile.toString() +" --> "+ newFile.toString());
	        	oldFile.renameTo(newFile);
	        	
	        	FileWriter fstream;
				try {
					fstream = new FileWriter(prop_file);
					BufferedWriter out = new BufferedWriter(fstream);
		    		out.write("path="+dir+
		    				"\nalbumArtist=VM" +
		    				"\ngenre=Bollywood Music" +
		    				"\nyear="+year+
		    				"\nmovie="+newName+"-"+year +
		    				"\nalbum="+newName +
		    				"\nreplace_file_name_by_album_tag="+replace_file_name_by_album_tag+
		    				"\nreplace_title_tag_as_filename="+replace_title_tag_as_filename+
		    				"\ntext1=");
		    				;
		    				
		    		for (int i=0; i<str2rem.length; i++){
		    			out.write(str2rem[i]+",");
		    		}
		    		
		    		out.write(newName);
		    		
		    		out.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
	    		  
	    		String myArgs[] = {prop_file}; 
	    		mp3TagEditor.MP3Editor.main(myArgs);
	    	}
	    	
	  	}
	}
}
