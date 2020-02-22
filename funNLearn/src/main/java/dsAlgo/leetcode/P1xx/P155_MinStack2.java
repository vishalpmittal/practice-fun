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

public class P155_MinStack2 {

	int min = 0;
	Stack<Integer> stack = null;

	/** initialize your data structure here. */
	public P155_MinStack2() {
		this.min = 0;
		this.stack = new Stack<Integer>();
	}

	/* Push the difference between min and current value
	 */
	public void push(int x) {
		if (stack.isEmpty()) {
			stack.push(0);
			min = x;
		} else {
			stack.push(x - min);
			if (x < min)
				min = x;
		}
	}

	/*
	 */
	public void pop() {
		if (stack.isEmpty())
			return;
		int pop = stack.pop();
		if (pop < 0)
			min = min - pop;
	}

	public int top() {
		int top = stack.peek();
		if (top > 0)
			return top + min;
		else
			return min;
	}

	public int getMin() {
		return min;
	}

	public static void main(String[] args) {

	}
}
