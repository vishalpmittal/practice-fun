package dsAlgo.leetcode.dependencies;

import java.util.HashMap;

@SuppressWarnings("serial")
public class CounterHashMap extends HashMap<Object, Integer> {

    int put(Object o) {
        if (this.get(o) != null) {
            this.put(o, 1);
            return 1;
        }
        this.put(o, this.get(o) + 1);
        return this.get(o);
    }

    int count(Object o) {
        return this.get(o);
    }
}
