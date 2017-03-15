package dsAlgo.lists;

public class LinkedList
{
   Node head = null;
   
   public LinkedList(){
      head = null;
   }
   
   public class Node
   {
      private String data;
      private Node next;      
      
      public Node()
      {
         this.data = "";
         this.next = null;
      }
      
      public Node(String data){
         this.data = data;
         this.next = null;
      }
      
      public Node(String data, Node next){
         this.data = data;
         this.next = next;
      }
      
      public String getData(){
         return this.data;
      }
      
      public Node getNext(){
         return this.next;
      }
      
      public void setData(String data){
         this.data = data; 
      }
      
      public void setNext(Node nextNode){
         this.next = nextNode;
      }
   }
   
   public void addData(){
      
   }
   
   public int getLength(){
      if(head==null)
         return 0;
      
      int count = 1;
      Node temp = head;
      
      while(temp.getNext()!=null)
      {
         count++;
         temp=temp.next;
      }
      return count;
   }
   
   public int printLL(){
      
      if (this.head == null)
         return -1;
      
      int count = 1;
      Node temp = head;
      
      while(temp.getNext()!=null)
      {
         System.out.println(temp.data);
         count++;
         temp=temp.next;
      }
      System.out.println(temp.data);
      return count;
   }
   
   
   
   
   public static void main(String args[])
   {
      LinkedList mylist = new LinkedList();
      
   }
   
   
}
