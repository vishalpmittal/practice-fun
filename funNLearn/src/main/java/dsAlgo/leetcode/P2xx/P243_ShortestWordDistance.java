/**
 * Tag: string, array
 * 
 * Given a list of words and two words word1 and word2, return the 
 * shortest distance between these two words in the list.
 * 
 * For example,
 * Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
 * 
 * Given word1 = “coding”, word2 = “practice”, return 3.
 * Given word1 = "makes", word2 = "coding", return 1.
 * 
 * Note:
 * You may assume that word1 does not equal to word2, and word1 and word2 
 * are both in the list.
 */

package dsAlgo.leetcode.P2xx;

import static org.junit.Assert.assertTrue;

public class P243_ShortestWordDistance {
	public static int shortestDistance(String[] words, String word1, String word2) {
		int dist = Integer.MAX_VALUE, loc1 = -1, loc2 = -1, i = 0;

		while (i < words.length) {
			if (words[i].compareTo(word1) == 0)
				loc1 = loc1 > i ? loc1 : i;
			if (words[i].compareTo(word2) == 0)
				loc2 = loc2 > i ? loc2 : i;

			if (loc1 != -1 && loc2 != -1) {
				int newDist = loc1 > loc2 ? loc1 - loc2 : loc2 - loc1;
				dist = newDist < dist ? newDist : dist;
			}
			i++;
		}
		return dist;
	}

	public static void main(String[] args) {
		String[] words = { "practice", "makes", "perfect", "coding", "makes" };
		assertTrue("Test1", shortestDistance(words, "coding", "practice") == 3);
		assertTrue("Test2", shortestDistance(words, "makes", "coding") == 1);

		System.out.println("All Tests passed");
	}
}
