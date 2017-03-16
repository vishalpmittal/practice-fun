/**
 * 
 */
package textgen;

import static org.junit.Assert.*;

import java.util.LinkedList;

import org.junit.Before;
import org.junit.Test;

/**
 * @author UC San Diego MOOC team
 *
 */
public class MyLinkedListTester {

	private static final int LONG_LIST_LENGTH =10; 

	MyLinkedList<String> shortList;
	MyLinkedList<Integer> emptyList;
	MyLinkedList<Integer> longerList;
	MyLinkedList<Integer> list1;
	
	/**
	 * @throws java.lang.Exception
	 */
	@Before
	public void setUp() throws Exception {
		// Feel free to use these lists, or add your own
	    shortList = new MyLinkedList<String>();
		shortList.add("A");
		shortList.add("B");
		emptyList = new MyLinkedList<Integer>();
		longerList = new MyLinkedList<Integer>();
		for (int i = 0; i < LONG_LIST_LENGTH; i++)
		{
			longerList.add(i);
		}
		list1 = new MyLinkedList<Integer>();
		list1.add(65);
		list1.add(21);
		list1.add(42);
	}

	
	/** Test if the get method is working correctly.
	 */
	/*You should not need to add much to this method.
	 * We provide it as an example of a thorough test. */
	@Test
	public void testGet()
	{
		//test empty list, get should throw an exception
		try {
			emptyList.get(0);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
			
		}
		
		// test short list, first contents, then out of bounds
		assertEquals("Check first", "A", shortList.get(0));
		assertEquals("Check second", "B", shortList.get(1));
		
		try {
			shortList.get(-1);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		try {
			shortList.get(2);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		// test longer list contents
		for(int i = 0; i<LONG_LIST_LENGTH; i++ ) {
			assertEquals("Check "+i+ " element", (Integer)i, longerList.get(i));
		}
		
		// test off the end of the longer array
		try {
			longerList.get(-1);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		
		}
		try {
			longerList.get(LONG_LIST_LENGTH);
			fail("Check out of bounds");
		}
		catch (IndexOutOfBoundsException e) {
		}
		
	}
	
	
	/** Test removing an element from the list.
	 * We've included the example from the concept challenge.
	 * You will want to add more tests.  */
	@Test
	public void testRemove()
	{
		// Add more tests here
		try {
			shortList.remove(-1);
			fail("Check remove Negative index");
		}catch (IndexOutOfBoundsException e) {}
		
		try {
			shortList.remove(2);
			fail("Check remove index not in range");
		}catch (IndexOutOfBoundsException e) {}

 	    String aStr = shortList.remove(0);
 	    assertEquals("Remove: check element 0 is correct ", "A", aStr);
 	    shortList.remove(0);
		assertEquals("Remove: check size is zero after removing all ", 0, shortList.size());
				
		int a = list1.remove(0);
		assertEquals("Remove: check a is correct ", 65, a);
		assertEquals("Remove: check element 0 is correct ", (Integer)21, list1.get(0));
		assertEquals("Remove: check size is correct ", 2, list1.size());
		
		try {
			emptyList.remove(0);
			fail("Check remove Empty List");
		}catch (IndexOutOfBoundsException e) {}		
		
 	    int b = longerList.remove(9);
 	    assertEquals("Remove: check last element", 9, b);
 	    assertEquals("Remove: last element, check size", 9, longerList.size());
 	    assertEquals("Remove: check new last element", (Integer)8, longerList.get(8));
 	    
 	    b = longerList.remove(4);
	    assertEquals("Remove: check middle element", 4, b);
	    assertEquals("Remove: middle element, check size", 8, longerList.size());
	    assertEquals("Remove: check new middle element", (Integer)5, longerList.get(4));
	}
	
	/** Test adding an element into the end of the list, specifically
	 *  public boolean add(E element)
	 * */
	@Test
	public void testAddEnd()
	{
        // implement this test
		try{
			shortList.add(null);
			fail("AddEnd: adding null value check");
		}catch(NullPointerException e){}
		
		boolean result = shortList.add("C");
		
		assertTrue("AddEnd: return value check", result);
		assertEquals("AddEnd: value check", "C", shortList.get(2));
		assertEquals("AddEnd: list size check", 3, shortList.size());
		assertEquals("AddEnd: last but one element check", "B", shortList.get(1));
		
		result = emptyList.add(1);
		assertTrue("AddEnd: emptyList, return value check", result);
		assertEquals("AddEnd: emptyList, value check", (Integer)1, emptyList.get(0));
		assertEquals("AddEnd: emptyList, list size check", 1, emptyList.size());
	}

	
	/** Test the size of the list */
	@Test
	public void testSize()
	{
		// implement this test
		assertEquals("testSize: emptyList, list size check", 0, emptyList.size());
		assertEquals("testSize: new list, list size check", 0, (new MyLinkedList<String>()).size());
		assertEquals("testSize: shortList, list size check", 2, shortList.size());
		assertEquals("testSize: longerList, list size check", 10, longerList.size());
		assertEquals("testSize: list1, list size check", 3, list1.size());
	}

	
	/** Test adding an element into the list at a specified index,
	 * specifically:
	 * public void add(int index, E element)
	 * */
	@Test
	public void testAddAtIndex()
	{
        // implement this test
		try{
			shortList.add(-1, "C");
			fail("testAddAtIndex: add outside the list range");
		}catch(IndexOutOfBoundsException e){}

		try{
			shortList.add(shortList.size()+1, "C");
			fail("testAddAtIndex: add outside the list range");
		}catch(IndexOutOfBoundsException e){}
		
		try{
			shortList.add(1, null);
			fail("testAddAtIndex: adding null value check");
		}catch(NullPointerException e){}

		list1.add(0, 11);
		assertEquals("testAddAtIndex: index 0, size check", 4, list1.size());
		assertEquals("testAddAtIndex: index 0, element check", (Integer)11, list1.get(0));
		assertEquals("testAddAtIndex: index 0, element check", (Integer)65, list1.get(1));

		list1.add(2, 23);
		assertEquals("testAddAtIndex: index 0, size check", 5, list1.size());
		assertEquals("testAddAtIndex: index 0, element check", (Integer)65, list1.get(1));
		assertEquals("testAddAtIndex: index 0, element check", (Integer)23, list1.get(2));
		assertEquals("testAddAtIndex: index 0, element check", (Integer)21, list1.get(3));
		
		longerList.add(10, 10);
		assertEquals("testAddAtIndex: index last, size check", 11, longerList.size());
		assertEquals("testAddAtIndex: index last, element check", (Integer)10, longerList.get(10));
		assertEquals("testAddAtIndex: index last, element check", (Integer)9, longerList.get(9));
	}
	
	/** Test setting an element in the list */
	@Test
	public void testSet()
	{
	    // implement this test
		try{
			shortList.set(-1, "C");
			fail("testSet: set outside the list range");
		}catch(IndexOutOfBoundsException e){}
		
		try{
			shortList.set(shortList.size(), "C");
			fail("testSet: set outside the list range");
		}catch(IndexOutOfBoundsException e){}

		try{
			shortList.set(shortList.size()+1, "C");
			fail("testSet: set outside the list range");
		}catch(IndexOutOfBoundsException e){}

		try{
			shortList.set(1, null);
			fail("testSet: set value null");
		}catch(NullPointerException e){}
		
		int oldVal = longerList.set(0, 100);
		assertEquals("testSet: index 0, size check", 10, longerList.size());
		assertEquals("testSet: index 0, old value", 0, oldVal);
		assertEquals("testSet: index 0, new value", (Integer)100, longerList.get(0));

		oldVal = longerList.set(longerList.size()-1, 109);
		assertEquals("testSet: index last, old value", 9, oldVal);
		assertEquals("testSet: index last, new value", (Integer)109, longerList.get(longerList.size()-1));

		oldVal = longerList.set(5, -105);
		assertEquals("testSet: index middle, old value", 5, oldVal);
		assertEquals("testSet: index middle, new value", (Integer)(-105), longerList.get(5));
	}
	
	// TODO: Optionally add more test methods.
	
}
