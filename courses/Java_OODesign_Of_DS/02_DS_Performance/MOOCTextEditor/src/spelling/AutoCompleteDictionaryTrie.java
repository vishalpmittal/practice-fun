package spelling;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * An trie data structure that implements the Dictionary and the AutoComplete
 * ADT
 * 
 * @author You
 *
 */
public class AutoCompleteDictionaryTrie implements Dictionary, AutoComplete {

	private TrieNode root;
	private int size;

	public AutoCompleteDictionaryTrie() {
		root = new TrieNode();
		size = 0;
	}

	/**
	 * Insert a word into the trie. For the basic part of the assignment (part
	 * 2), you should ignore the word's case. That is, you should convert the
	 * string to all lower case as you insert it.
	 */
	public boolean addWord(String word) {
		// TODO: Implement this method.
		if (word.trim().compareTo("") == 0)
			return false;

		TrieNode currNode = root;
		for (int i = 0; i < word.length(); i++) {
			char lchar = Character.toLowerCase(word.charAt(i));
			if (currNode.getChild(lchar) == null){
				currNode = currNode.insert(lchar);
				currNode.setText("");
			}
			else
				currNode = currNode.getChild(lchar);
		}

		if (currNode.endsWord() && currNode.getText().compareTo(word.toLowerCase()) == 0)
			return false;

		currNode.setEndsWord(true);
		currNode.setText(word.toLowerCase());
		this.size++;

		return true;
	}

	/**
	 * Return the number of words in the dictionary. This is NOT necessarily the
	 * same as the number of TrieNodes in the trie.
	 */
	public int size() {
		// TODO: Implement this method
		return this.size;
	}

	/** Returns whether the string is a word in the trie */
	@Override
	public boolean isWord(String s) {
		// TODO: Implement this method
		if (this.size == 0 || s.trim().compareTo("") == 0)
			return false;

		TrieNode currNode = root;
		for (int i = 0; i < s.length(); i++) {
			char lchar = Character.toLowerCase(s.charAt(i));
			if (currNode.getChild(lchar) == null)
				return false;
			else
				currNode = currNode.getChild(lchar);
		}
		if (currNode.getText().compareTo(s.toLowerCase()) == 0)
			return true;

		return false;
	}

	/**
	 * * Returns up to the n "best" predictions, including the word itself, in
	 * terms of length If this string is not in the trie, it returns null.
	 * 
	 * @param text
	 *            The text to use at the word stem
	 * @param n
	 *            The maximum number of predictions desired.
	 * @return A list containing the up to n best predictions
	 */
	@Override
	public List<String> predictCompletions(String prefix, int numCompletions) {
		// TODO: Implement this method
		// This method should implement the following algorithm:
		// 1. Find the stem in the trie. If the stem does not appear in the
		// trie, return an empty list
		// 2. Once the stem is found, perform a breadth first search to generate
		// completions using the following algorithm:
		// Create a queue (LinkedList) and add the node that completes the stem
		// to the back of the list.
		// Create a list of completions to return (initially empty)
		// While the queue is not empty and you don't have enough completions:
		// remove the first Node from the queue
		// If it is a word, add it to the completions list
		// Add all of its child nodes to the back of the queue
		// Return the list of completions
		List<String> predictions = new ArrayList<String>();
		if (this.size == 0 || numCompletions < 1)
			return predictions;

		TrieNode currNode = root;
		for (int i = 0; i < prefix.length(); i++) {
			char lchar = Character.toLowerCase(prefix.charAt(i));
			if (currNode.getChild(lchar) == null)
				return predictions;
			else
				currNode = currNode.getChild(lchar);
		}

		Queue<TrieNode> traverseq = new LinkedList<TrieNode>();
		traverseq.add(currNode);

		while (traverseq.size() > 0 && predictions.size() < numCompletions) {
			TrieNode travNode = traverseq.remove();
			if (travNode.endsWord() && travNode.getText().compareTo("") != 0)
				predictions.add(travNode.getText());
			for (char c : travNode.getValidNextCharacters()) {
				traverseq.add(travNode.getChild(c));
			}
		}
		return predictions;
	}

	// For debugging
	public void printTree() {
		printNode(root);
	}

	/** Do a pre-order traversal from this node down */
	public void printNode(TrieNode curr) {
		if (curr == null)
			return;

		System.out.print("Text: "+ curr.getText());
		System.out.println("; Child Nodes: " + curr.getValidNextCharacters().toString());

		TrieNode next = null;
		for (Character c : curr.getValidNextCharacters()) {
			next = curr.getChild(c);
			printNode(next);
		}
	}

}