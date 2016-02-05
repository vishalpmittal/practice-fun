package java.concurrent;

class Account{
   int balance = 390;
   Object obj = new Object();
   
   public void withdrow(int amount){
      synchronized(this)
      {
         if (balance - amount > 0)
         {
            balance -= amount;
            System.out.println("Withdraw 100 by:"+ Thread.currentThread().getName());
         }
      }
   }
   
   public void withdrow1(int amount){
      synchronized(obj)
      {
         if (balance - amount > 0)
            balance -= amount;
      }
   }

   public synchronized void withdrow2(int amount){
      if (balance - amount > 0)
         balance -= amount;
   }   
}

class Withdrawer extends Thread{
   Account acc;
   public void run(){
      for (int i=0; i<5; i++)
         acc.withdrow(100);
   }
}

public class AccSyncThread
{
   public static void main(String[] args)
   {
      Account acc = new Account ();
      Withdrawer w1 = new Withdrawer();
      Withdrawer w2 = new Withdrawer();
      w1.setName("W1");
      w2.setName("W2");
      w1.acc = acc;
      w2.acc = acc;
      
      w1.start();
      w2.start();
   }
}