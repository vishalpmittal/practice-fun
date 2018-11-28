package javaMisc.concurrent.exampleRunnable;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;


public class UserStressTest implements Runnable
{
   public void testURL() throws Exception {
      String strUrl = "http://www.google.com";

      try {
          URL url = new URL(strUrl);
          HttpURLConnection urlConn = (HttpURLConnection) url.openConnection();
          urlConn.connect();
          
          if (urlConn.getResponseCode() == HttpURLConnection.HTTP_OK)
             System.out.println(Thread.currentThread().getName()+"Connected");
          
          System.out.println(urlConn.getDate());
          
      } catch (IOException e) {
          System.err.println("Error creating HTTP connection");
          e.printStackTrace();
          throw e;
      }
  }
   
   public void run(){
      try
      {
         this.testURL();
      } catch (Exception e)
      {
         e.printStackTrace();
      }
   }
   
   public static void main(String args[]){
      UserStressTest test = new UserStressTest();
      for (int i=0; i<10; i++)
      {
         Thread t = new Thread(test, "t"+i);
         t.start();
      }
   }
   
}
