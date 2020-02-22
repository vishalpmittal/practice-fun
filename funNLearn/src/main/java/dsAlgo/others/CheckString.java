package dsAlgo.others;
import java.util.ArrayList;
import java.util.List;

/*
 * /myString = { "Barge", "larry", "dan", "marshall", "arch", "sarah", "jessica", "steven","sharp", "darKo", "carl", "matthew", "charm” }
 *  Given a array of strings myStrings, parse through that list and 
 *  return each index within that list 
 * - that sequentially contains ‘ar’,
 * - is at least 5 characters in length and 
 * - does not have a Capital letter..
 */

public class CheckString {

    public static List<Integer> checkMyStrings(String[] mystrs) {
        List<Integer> retList = new ArrayList<Integer>();
        if (mystrs.length == 0) {
            return retList;
        }

        for (int i = 0; i < mystrs.length; i++) {

            // Check if length >= 5
            if (mystrs[i].trim().length() >= 5) {

                boolean hasCapitol = false;
                boolean hasSequence = false;
                boolean wasA = false;

                // Iterate for each character in that string
                for (char c : mystrs[i].toCharArray()) {
                    // check if not capitol
                    if (Character.isUpperCase(c)) {
                        hasCapitol = true;
                    } else {
                        // check for sequence
                        if (c == 'a') {
                            wasA = true;
                        } else if (c == 'r' && wasA == true) {
                            hasSequence = true;
                        } else {
                            wasA = false;
                        }
                    }
                } // for
                if (!hasCapitol && hasSequence) {
                    retList.add(i);
                }
            }
        }
        return retList;
    }

    public static void main(String args[]) {
        String[] myString = { "Barge", "larry", "dan", "marshall", "arch", "sarah", "jessica", "steven", "sharp",
                "darKo", "carl", "matthew", "charm" };

        System.out.println(checkMyStrings(myString));
    }
}
