package textgen;

import java.util.AbstractList;


/** A class that implements a doubly linked list
 * 
 * @author UC San Diego Intermediate Programming MOOC team
 *
 * @param <E> The type of the elements stored in the list
 */
public class MyLinkedList<E> extends AbstractList<E> {
	LLNode<E> head;
	LLNode<E> tail;
	int size;

	/** Create a new empty LinkedList */
	public MyLinkedList() {
		// Implement this method
		this.head = new LLNode<E>(null);
		this.tail = new LLNode<E>(null);
		
		this.head.next = this.tail;
		this.tail.prev = this.head;
		size = 0;
	}

	/**
	 * Appends an element to the end of the list
	 * @param element The element to add
	 */
	public boolean add(E element ) 
	{
		if (element == null)
			throw new NullPointerException();
			
		// Implement this method
		new LLNode<E>(element, this.tail.prev);
		this.size++;
		return true;
	}

	/** Get the element at position index 
	 * @throws IndexOutOfBoundsException if the index is out of bounds. */
	public E get(int index) 
	{
		// Implement this method.
		LLNode<E> anchor = this.getNodeAnchor(index);
		return anchor.data;
	}

	/**
	 * Add an element to the list at the specified index
	 * @param The index where the element should be added
	 * @param element The element to add
	 */
	public void add(int index, E element ) 
	{
		// Implement this method
		if (element == null)
			throw new NullPointerException();
		
		if (index == this.size()){
			this.add(element);
			return;
		}
		LLNode<E> anchor = this.getNodeAnchor(index);
		new LLNode<E>(element, anchor.prev);
		this.size++;
	}


	/** Return the size of the list */
	public int size() 
	{
		// Implement this method
		return this.size;
	}

	/** Remove a node at the specified index and return its data element.
	 * @param index The index of the element to remove
	 * @return The data element removed
	 * @throws IndexOutOfBoundsException If index is outside the bounds of the list
	 * 
	 */
	public E remove(int index) 
	{
		// Implement this method
		LLNode<E> anchor = this.getNodeAnchor(index);
		anchor.prev.next = anchor.next;
		anchor.next.prev = anchor.prev;
		this.size--;
		return anchor.data;
	}

	/**
	 * Set an index position in the list to a new element
	 * @param index The index of the element to change
	 * @param element The new element
	 * @return The element that was replaced
	 * @throws IndexOutOfBoundsException if the index is out of bounds.
	 */
	public E set(int index, E element) 
	{
		// Implement this method
		LLNode<E> anchor = this.getNodeAnchor(index);
		E returnVal = anchor.data;
		if (returnVal == null || element == null){
			throw new NullPointerException();
		}
		anchor.data = element;
		return returnVal;
	}   

	/** Helper method to get a pointer to specific node. */
	private LLNode<E> getNodeAnchor(int index){
		if (index >= this.size || index < 0){
			throw new IndexOutOfBoundsException();
		}
		
		LLNode<E> anchor = this.head.next;
		int anchorIndx = 0;
		while (anchorIndx < index){
			anchor = anchor.next;
			anchorIndx++;
		}
		return anchor;
	}

	public String toString(){
		if (this.size == 0)
			return "[ ]"; 
		StringBuilder sb = new StringBuilder("[ ");
		
		LLNode<E> anchor = this.head.next;

		while (anchor.next.next != null){
			sb.append(anchor.data.toString() + ", ");
			anchor = anchor.next;
		}
		sb.append(anchor.data.toString()+ " ]");
		return sb.toString();
	}
}

class LLNode<E> 
{
	LLNode<E> prev;
	LLNode<E> next;
	E data;

	// Add any other methods you think are useful here
	// E.g. you might want to add another constructor
	
	public LLNode(E e) 
	{
		this.data = e;
		this.prev = null;
		this.next = null;
	}
	
	public LLNode(E e, LLNode<E> prev){
		this.data = e;
		prev.next.prev = this;
		this.next = prev.next;
		this.prev = prev;
		prev.next = this;
	}
	
	public String toString(){
		return this.data.toString();
	}
	
}
