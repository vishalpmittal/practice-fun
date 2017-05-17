package dsAlgo.todo;

import java.util.Comparator;
import java.util.HashMap;
import java.util.TreeMap;
import java.util.Map.Entry;

public class ValueSortedMap {

    static Comparator<Entry<String, Integer>> valueComparator = new Comparator<Entry<String, Integer>>() {
        @Override
        public int compare(Entry<String, Integer> e1, Entry<String, Integer> e2) {
            return Integer.compare(e1.getValue(), e2.getValue());
        }
    };

    
    
    
}
