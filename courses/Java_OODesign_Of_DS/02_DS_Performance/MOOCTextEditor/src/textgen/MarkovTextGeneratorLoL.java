package textgen;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.Random;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/** 
 * An implementation of the MTG interface that uses a list of lists.
 * @author UC San Diego Intermediate Programming MOOC team 
 */
public class MarkovTextGeneratorLoL implements MarkovTextGenerator {

	// The list of words with their next words
	private List<ListNode> wordList; 
	
	// The starting "word"
	private String starter;
	
	// The random number generator
	private Random rnGenerator;
	
	private boolean trained = false;
	
	public MarkovTextGeneratorLoL(Random generator)
	{
		wordList = new LinkedList<ListNode>();
		starter = "";
		rnGenerator = generator;
	}
	
	
	/** Train the generator by adding the sourceText */
	@Override
	public void train(String sourceText)
	{
		// Implement this method
		if (sourceText==null || sourceText.trim().compareTo("")==0){
			return;
		}

		List<String> words = this.getWords(sourceText);
		starter = words.get(0);
		words.add(words.get(0));
		String prevWord = words.get(0);
		
		for (int i=1; i<words.size(); i++){
			ListNode prevWordNode = getListNode(prevWord);
			if (prevWordNode == null){
				prevWordNode = new ListNode(prevWord);
				this.wordList.add(prevWordNode);
			}
			prevWordNode.addNextWord(words.get(i));
			prevWord = words.get(i);
		}
		
		trained = true;
	}
	
	/** 
	 * Generate the number of words requested.
	 */
	@Override
	public String generateText(int numWords) {
	    // Implement this method
		if(!trained){
			return "";
		}
		
		if (numWords<1)
			return "";
		
		String currWord = this.starter;
		StringBuilder output = new StringBuilder(currWord + " ");
		int outputLen = 1;
		while (outputLen < numWords){
			ListNode currWordNode = getListNode(currWord);
			String randomWord = currWordNode.getRandomNextWord(this.rnGenerator);
			output.append(randomWord + " ");
			currWord = randomWord;
			outputLen++;
		}
		return output.toString();
	}
	
	
	// Can be helpful for debugging
	@Override
	public String toString()
	{
		String toReturn = "";
		for (ListNode n : wordList)
		{
			toReturn += n.toString();
		}
		return toReturn;
	}
	
	/** Retrain the generator from scratch on the source text */
	@Override
	public void retrain(String sourceText)
	{
		// Implement this method.
		this.wordList = new LinkedList<ListNode>();
		this.starter = "";
		this.trained = false;
		this.train(sourceText);
	}
	
	// Add any private helper methods you need here.
	private List<String> getWords(String text)
	{
		String wordsArray[] = text.split("\\s+");
		ArrayList<String> tokens = new ArrayList<String>();
		Collections.addAll(tokens, wordsArray);
		
		return tokens;
	}
	
	private ListNode getListNode(String word){
		for (ListNode anchor: wordList){
			if (anchor.getWord().compareTo(word)==0)
				return anchor;
		}
		return null;
	}
	
	
	/**
	 * This is a minimal set of tests.  Note that it can be difficult
	 * to test methods/classes with randomized behavior.   
	 * @param args
	 */
	public static void main(String[] args)
	{
		// feed the generator a fixed random value for repeatable behavior
		MarkovTextGeneratorLoL gen = new MarkovTextGeneratorLoL(new Random(42));
		String textString = "Hello.  Hello there.  This is a test.  Hello there.  Hello Bob.  Test again.";
		System.out.println(textString);
		gen.train(textString);
		gen.train("vishal is great");
		System.out.println(gen);
		System.out.println(gen.generateText(20));
		
		
		String textString2 = "You say yes, I say no, "+
				"You say stop, and I say go, go, go, "+
				"Oh no. You say goodbye and I say hello, hello, hello, "+
				"I don't know why you say goodbye, I say hello, hello, hello, "+
				"I don't know why you say goodbye, I say hello. "+
				"I say high, you say low, "+
				"You say why, and I say I don't know. "+
				"Oh no. "+
				"You say goodbye and I say hello, hello, hello. "+
				"I don't know why you say goodbye, I say hello, hello, hello, "+
				"I don't know why you say goodbye, I say hello. "+
				"Why, why, why, why, why, why, "+
				"Do you say goodbye. "+
				"Oh no. "+
				"You say goodbye and I say hello, hello, hello. "+
				"I don't know why you say goodbye, I say hello, hello, hello, "+
				"I don't know why you say goodbye, I say hello. "+
				"You say yes, I say no, "+
				"You say stop and I say go, go, go. "+
				"Oh, oh no. "+
				"You say goodbye and I say hello, hello, hello. "+
				"I don't know why you say goodbye, I say hello, hello, hello, "+
				"I don't know why you say goodbye, I say hello, hello, hello, "+
				"I don't know why you say goodbye, I say hello, hello, hello,";
		System.out.println(textString2);
		gen.retrain(textString2);
		System.out.println(gen);
		System.out.println(gen.generateText(20));
		
		gen.retrain("");
		System.out.println(gen);
		System.out.println(gen.generateText(20));
	}

}

/** Links a word to the next words in the list 
 * You should use this class in your implementation. */
class ListNode
{
    // The word that is linking to the next words
	private String word;
	
	// The next words that could follow it
	private List<String> nextWords;
	
	ListNode(String word)
	{
		this.word = word;
		nextWords = new LinkedList<String>();
	}
	
	public String getWord()
	{
		return word;
	}

	public void addNextWord(String nextWord)
	{
		nextWords.add(nextWord);
	}
	
	public String getRandomNextWord(Random generator)
	{
		// Implement this method
	    // The random number generator should be passed from 
	    // the MarkovTextGeneratorLoL class
		return nextWords.get(generator.nextInt(nextWords.size()));
	}

	public String toString()
	{
		String toReturn = word + ": ";
		for (String s : nextWords) {
			toReturn += s + "->";
		}
		toReturn += "\n";
		return toReturn;
	}
	
}


