/**
 * Tag: stack
 * 
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
 * determine if the input string is valid.
 * The brackets must close in the correct order, "()" and "()[]{}" are all valid 
 * but "(]" and "([)]" are not.
 */

package leetcode.algorithms.P001_P100;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.assertTrue;

import java.util.HashMap;
import java.util.Stack;

import static org.junit.Assert.assertFalse;

public class P020_ValidParentheses {
	public static boolean isValid(String s) {
		HashMap<Character, Character> brkts = new HashMap<Character, Character>();
		brkts.put('{', '}');
		brkts.put('(', ')');
		brkts.put('[', ']');

		Stack<Character> stack = new Stack<Character>();

		for (int i = 0; i < s.length(); i++) {
			if (!stack.isEmpty() && s.charAt(i) == brkts.get(stack.peek()))
				stack.pop();
			else if (!brkts.keySet().contains(s.charAt(i)))
				return false;
			else
				stack.push(s.charAt(i));
		}
		return stack.isEmpty();
	}

	@Test
	public void test() {
		assertTrue("Test1", isValid("(){}[]"));
		assertTrue("Test1", isValid("({[{[]}]})"));
		assertFalse("Test2", isValid("({[[]}])"));
	}

	public static void main(String[] args) {
		Result result = JUnitCore.runClasses(P020_ValidParentheses.class);
		System.out.println("All Tests passed : " + result.wasSuccessful());
		for (Failure failure : result.getFailures()) {
			System.out.println("Failed Test cases" + failure.toString());
		}
	}
}
