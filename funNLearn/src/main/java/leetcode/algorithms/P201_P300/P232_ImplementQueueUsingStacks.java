/*
 * Implement the following operations of a queue using stacks.
 * 
 * push(x) -- Push element x to the back of queue.
 * pop() -- Removes the element from in front of queue.
 * peek() -- Get the front element.
 * empty() -- Return whether the queue is empty.
 * 
 * Notes:
 * You must use only standard operations of a stack -- which means only push to top, 
 * peek/pop from top, size, and is empty operations are valid.
 * Depending on your language, stack may not be supported natively. 
 * You may simulate a stack by using a list or deque (double-ended queue), as long as 
 * you use only standard operations of a stack.
 * You may assume that all operations are valid (for example, no pop or peek 
 * operations will be called on an empty queue).
 */

package leetcode.algorithms.P201_P300;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;

import java.util.Stack;

import static org.junit.Assert.assertFalse;

class MyQueue {
	Stack<Integer> dataStack = new Stack<Integer>();
	Stack<Integer> helperStack = new Stack<Integer>();

	// Push element x to the back of queue.
	public void push(int x) {
		while (!dataStack.isEmpty())
			helperStack.push(dataStack.pop());

		dataStack.push(x);

		while (!helperStack.isEmpty())
			dataStack.push(helperStack.pop());
	}

	// Removes the element from in front of queue.
	public void pop() {
		dataStack.pop();
	}

	// Get the front element.
	public int peek() {
		return dataStack.peek();
	}

	// Return whether the queue is empty.
	public boolean empty() {
		return dataStack.isEmpty();
	}
}

class MyQueue_1 {
	Stack<Integer> s1 = new Stack<Integer>();
	Stack<Integer> s2 = new Stack<Integer>();

	// Push element x to the back of queue.
	public void push(int x) {
		s1.push(x);
	}

	// Removes the element from in front of queue.
	public void pop() {
		this.peek();
		s2.pop();
	}

	// Get the front element.
	public int peek() {
		if (s2.empty())
			while (!s1.empty())
				s2.push(s1.pop());
		return s2.peek();
	}

	// Return whether the queue is empty.
	public boolean empty() {
		return s1.empty() && s2.empty();
	}
}

public class P232_ImplementQueueUsingStacks {
	@Test
	public void test() {
		MyQueue_1 q1 = new MyQueue_1();
		assertTrue("Test1", q1.empty());

		q1.push(1);
		q1.push(2);
		q1.push(3);
		assertTrue("Test2", q1.peek() == 1);

		q1.pop();
		assertTrue("Test3", q1.peek() == 2);

		assertFalse("Test4", q1.empty());
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P232_ImplementQueueUsingStacks.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
