/**
 * Tag: list
 *
 * Design a stack that supports push, pop, top, and retrieving the 
 * minimum element in constant time.
 * 
 * push(x) -- Push element x onto stack.
 * pop() -- Removes the element on top of the stack.
 * top() -- Get the top element.
 * getMin() -- Retrieve the minimum element in the stack.
 * 
 * Example:
 * MinStack minStack = new MinStack();
 * minStack.push(-2);
 * minStack.push(0);
 * minStack.push(-3);
 * minStack.getMin();   --> Returns -3.
 * minStack.pop();
 * minStack.top();      --> Returns 0.
 * minStack.getMin();   --> Returns -2.
 */

package dsAlgo.leetcode.P1xx;

import java.util.Stack;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class P155_MinStack {

	int min = 0;
	Stack<Integer> stack = null;

	/** initialize your data structure here. */
	public P155_MinStack() {
		this.min = Integer.MAX_VALUE;
		this.stack = new Stack<Integer>();
	}

	/*
	 * Push the first value in stack as is
	 * if new minimum needs to be pushed, push the old minimum value and 
	 * then new minimum value on top of it. So in short we push two values (current min and new x)
	 * when popping a min value we pop the top and we pop the next one and set it as next min
	 */
	public void push(int x) {
		if (x <= min) {
			stack.push(min);
			min = x;
		}
		stack.push(x);
	}

	/*
	 * if popping a min value pop two times and the second one should be our next min value
	 */
	public void pop() {
		if (stack.peek() == min) {
			stack.pop();
			min = stack.peek();
			stack.pop();
		} else {
			stack.pop();
		}
		if (stack.isEmpty()) {
			min = Integer.MAX_VALUE;
		}
	}

	public int top() {
		return stack.peek();
	}

	public int getMin() {
		return min;
	}

	@Test
	public void test() {
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P155_MinStack.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
