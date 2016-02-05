package dsAlgo.lists;

public class SingleLinkedListTest
{
   public static void main(String args[]){
      SingleLinkedList list1 = new SingleLinkedList();

      list1.insert(null);
      list1.insert(list1.new Node("L"));
      list1.insert(list1.new Node("A"));
      list1.insert(list1.new Node("H"));
      list1.insert(list1.new Node("S"));
      list1.insert(list1.new Node("I"));
      list1.insert(list1.new Node("V"));
      list1.printLL();
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");
      
      list1.insertEOL(null);
      list1.insertEOL(list1.new Node("M"));
      list1.insertEOL(list1.new Node("I"));
      list1.insertEOL(list1.new Node("T"));
      list1.insertEOL(list1.new Node("T"));
      list1.insertEOL(list1.new Node("A"));
      list1.insertEOL(list1.new Node("L"));
      list1.printLL();
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");
      
      list1.insertAtN(-3, list1.new Node(" "));
      list1.insertAtN(0, list1.new Node(" "));
      list1.insertAtN(1, list1.new Node("Mr."));
      list1.insertAtN(8, null);
      
      SingleLinkedList.Node commaNode = list1.new Node(",");
      list1.insertAtN(8, commaNode);
      list1.insertAtN(15, list1.new Node("."));
      list1.insertAtN(17, list1.new Node("."));
      list1.printLL();
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");
      
      System.out.println("removed : "+ list1.removeFirst().data());
      list1.printLL();
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");
      
      System.out.println("removed : "+ list1.removeLast().data());
      list1.printLL();
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");
      
      System.out.println("removed : "+ list1.removeNth(7).data());
      list1.printLL();
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");
      
      
      list1.insertAtN(7, commaNode);
      list1.printLL();
      System.out.println("\nremoved : "+commaNode.data() +" at "+ list1.removeNode(commaNode));
      list1.printLL();
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");

      list1.insertEOL(list1.new Node("."));
      System.out.println("Middle : "+ list1.getMiddle().data());
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");

      System.out.println("First : "+ list1.getNthNode(1).data());
      System.out.println("Fifth : "+ list1.getNthNode(5).data());
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");
      
      System.out.println("First : "+ list1.getNthFromEnd(10).data());
      System.out.println("Fifth : "+ list1.getNthFromEnd(7).data());
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");
      
      System.out.println("reverse head :"+list1.reverseList().data());
      list1.printLL();
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");

      System.out.println("reverse head :"+list1.reverseList().data());
      list1.printLL();
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");

      SingleLinkedList.Node endNode = list1.getTail();
      endNode.setNext(list1.head);
      System.out.println("is loop : "+ list1.isLoop());
      endNode.setNext(list1.head.next());
      System.out.println("is loop : "+ list1.isLoop());
      endNode.setNext(null);
      list1.insertAtN(7, commaNode);
      System.out.println("is loop : "+ list1.isLoop());
      endNode.setNext(commaNode);
      System.out.println("is loop : "+ list1.isLoop());
      endNode.setNext(null);
      
      list1.printLL();
      System.out.println("\nLength:"+list1.getLength());
      System.out.println("\n-------------------------------------------");

      // Sorted Insert Test
      SingleLinkedList list2 = new SingleLinkedList();
      list2.sortedInsert(list2.new Node("V"));
      list2.sortedInsert(list2.new Node("I"));
      list2.sortedInsert(list2.new Node("S"));
      list2.sortedInsert(list2.new Node("H"));
      list2.sortedInsert(list2.new Node("A"));
      list2.sortedInsert(list2.new Node("L"));
      list2.printLL();
      System.out.println("\nLength:"+list2.getLength());
      System.out.println("\n-------------------------------------------");
      
      // List Append test
      SingleLinkedList list3 = new SingleLinkedList();
      SingleLinkedList list4 = new SingleLinkedList();
      list3.append(list4.head);
      
      list3.insertEOL(list1.new Node("V"));
      list3.insertEOL(list1.new Node("I"));
      list3.insertEOL(list1.new Node("S"));
      list3.insertEOL(list1.new Node("H"));
      list3.append(list4.head);
      
      list4.insertEOL(list1.new Node("M"));
      list4.insertEOL(list1.new Node("I"));
      list4.insertEOL(list1.new Node("T"));
      list4.insertEOL(list1.new Node("T"));
      list3.append(list4.head);

      list3.printLL();
      System.out.println("\nLength:"+list3.getLength());
      System.out.println("\n-------------------------------------------");

      // List Split test
      SingleLinkedList list5 = new SingleLinkedList();
      SingleLinkedList list6 = new SingleLinkedList();
      
      list5.insertEOL(list5.new Node("V"));
      list5.insertEOL(list5.new Node("I"));
      list5.insertEOL(list5.new Node("S"));
      list5.insertEOL(list5.new Node("H"));
      list5.insertEOL(list5.new Node("M"));
      list5.insertEOL(list5.new Node("I"));
      list5.insertEOL(list5.new Node("T"));
      list5.insertEOL(list5.new Node("T"));
      
      list6.head = list5.split(5);

      list5.printLL();
      System.out.println("\nLength:"+list5.getLength());
      list6.printLL();
      System.out.println("\nLength:"+list6.getLength());
      System.out.println("\n-------------------------------------------");
      
      // Alternate Split test
      SingleLinkedList list7 = new SingleLinkedList();
      SingleLinkedList list8 = new SingleLinkedList();
      
      list7.insertEOL(list7.new Node("V"));
      list7.insertEOL(list7.new Node("I"));
      list7.insertEOL(list7.new Node("S"));
      list7.insertEOL(list7.new Node("H"));
      list7.insertEOL(list7.new Node("M"));
      list7.insertEOL(list7.new Node("I"));
      list7.insertEOL(list7.new Node("T"));
      list7.insertEOL(list7.new Node("T"));
      
      list8.head = list7.alternateSplit();

      list7.printLL();
      System.out.println("\nLength:"+list7.getLength());
      list8.printLL();
      System.out.println("\nLength:"+list8.getLength());
      System.out.println("\n-------------------------------------------");
      
      
      // Rotate right test
      SingleLinkedList list9 = new SingleLinkedList();
      
      list9.insertEOL(list9.new Node("V"));
      list9.insertEOL(list9.new Node("I"));
      list9.insertEOL(list9.new Node("S"));
      list9.insertEOL(list9.new Node("H"));
      list9.insertEOL(list9.new Node("M"));
      list9.insertEOL(list9.new Node("I"));
      list9.insertEOL(list9.new Node("T"));
      list9.insertEOL(list9.new Node("T"));
      list9.rotateRight(3);
      list9.printLL();
      System.out.println("\nLength:"+list9.getLength());
      System.out.println("\n-------------------------------------------");
      
      // Rotate left test
      list9.rotateLeft(4);
      list9.printLL();
      System.out.println("\nLength:"+list9.getLength());
      System.out.println("\n-------------------------------------------");
      
      // Rotate right test
      list8.head = null;
      list9.head = null;
            
      list8.insertEOL(list8.new Node("V"));
      list9.insertEOL(list9.new Node("I"));
      list8.insertEOL(list8.new Node("S"));
      list9.insertEOL(list9.new Node("H"));
      list8.insertEOL(list8.new Node("M"));
      list9.insertEOL(list9.new Node("I"));
      list8.insertEOL(list8.new Node("T"));
      list9.insertEOL(list9.new Node("T"));

      list8.shuffleMerge(list9.head);
      list8.printLL();
      System.out.println("\nLength:"+list8.getLength());
      System.out.println("\n-------------------------------------------");
      
      }
}
