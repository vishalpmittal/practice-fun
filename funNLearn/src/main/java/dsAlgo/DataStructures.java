package dsAlgo;

// import java.util.Collection; //Interface

// --------------------------------------
// import java.util.List; // Interface implements Collection
// --------------------------------------
import java.util.ArrayList;

// --------------------------------------
// import java.util.Queue; // Interface implements Collection
// --------------------------------------
import java.util.LinkedList; // implements both Queue and List
import java.util.PriorityQueue;

// --------------------------------------
// import java.util.Set; // Interface implements Collection
// --------------------------------------
// import java.util.SortedSet; // Interface
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.TreeSet;

// --------------------------------------
import java.util.Map;
// --------------------------------------
// import java.util.SortedMap; // Interface
import java.util.HashMap;
import java.util.Hashtable;
import java.util.TreeMap;
import java.util.LinkedHashMap;

import java.util.Iterator;
import java.util.Arrays;
// import java.util.Collections;
import java.util.Comparator;

class Student {
    String name;

    public Student(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }
}

class StudentComparator implements Comparator<Student> {
    public int compare(Student s1, Student s2) {
        return s1.getName().compareTo(s2.getName());
    }
}

public class DataStructures {

    public static void main(String args[]) {
        DataStructures ds = new DataStructures();
        ds.string_demo();
        ds.array();
        ds.arrayList();
        ds.multiDimensionalArray();

        ds.linkedList();
        ds.stack();
        ds.queue();

        ds.priorityQueue();
        ds.dequeue();

        ds.hashSet();
        ds.treeSet();
        ds.linkedHashSet();

        ds.hashTable();
        ds.hashMap();
        ds.linkedHashMap();
        ds.treeMap();
    }

    public void string_demo() {
        String S = "vishal";

        for (int i = 0; i < S.length(); i++) {
            System.out.println(S.charAt(i));
        }

        for (char c : S.toCharArray()) {
            System.out.println(c);
        }

        for (String ch : S.split("")) {
            System.out.println(ch);
        }

        S.chars().forEach(i -> System.out.println(Character.toChars(i)));

        // --->> Gets
        // charAt(int index); -> char
        // indexOf(String str);
        // indexOf(String str, int fromIndex);
        // lastIndexOf(int ch, int fromIndex) -> int
        // lastIndexOf(String str, int fromIndex) -> int
        // substring(int beginIndex, int endIndex)

        // --->> Checks
        // isEmpty() -> bool
        // equals(Object anObject); -> int
        // equalsIgnoreCase(String anotherString); -> int
        // compareTo(String anotherString); -> int
        // compareToIgnoreCase(String str); -> int
        // contains(CharSequence s); -> bool
        // endsWith(String suffix); -> bool
        // startsWith(String prefix)
        // matches(String regex)

        // --->> operations
        // concat(String str);
        // join(CharSequence delimiter, CharSequence... elements) -> String
        // split(String regex)
        // split(String regex, int limit)

        // --->> Update in place
        // replace(char oldChar, char newChar)
        // replace(CharSequence target, CharSequence replacement)
        // replaceAll(String regex, String replacement)
        // replaceFirst(String regex, String replacement)
        // toLowerCase()
        // toUpperCase()
        // trim()

    }

    // --------------arrays-----------------

    public void array() {
        int[] myNum = { 10, 20, 30, 40 }; // with predefined list
        int[] myNum1 = new int[10]; // with length 10

        String[] cars = { "Volvo", "BMW", "Ford", "Mazda" };

        for (int i = 0; i < cars.length; i++)
            System.out.println(cars[i]);

        for (String i : cars)
            System.out.println(i);

        int i = 0;
        while (i < cars.length)
            System.out.println(cars[i]);

        Arrays.binarySearch(myNum, 1);
        Arrays.copyOf(myNum1, 10);
        Arrays.equals(myNum, myNum1);
        Arrays.copyOfRange(myNum, 1, 4);

        Student[] stdArray = { new Student("a"), new Student("b"), new Student("c"), new Student("d") };
        Arrays.sort(stdArray, new StudentComparator());
    }

    public void arrayList() {
        ArrayList<Integer> al = new ArrayList<Integer>();
        al.add(1);
        al.contains(1);
        al.indexOf(1);
        al.isEmpty();
        al.remove(0); // index
        al.get(0); // index
        al.size();

        for (int i = 0; i < al.size(); i++)
            System.out.println(al.get(i));

        for (int x : al)
            System.out.println(x);

        int i = 0;
        while (i < al.size())
            System.out.println(al.get(i));

        Iterator<Integer> it = al.iterator();
        while (it.hasNext())
            System.out.println(it.next());
    }

    public void multiDimensionalArray() {
        int[][] myNumbers1 = new int[4][5];
        System.out.println(myNumbers1);

        int[][] myNumbers = { { 1, 2, 3, 4 }, { 5, 6, 7 } };
        for (int i = 0; i < myNumbers.length; ++i) {
            for (int j = 0; j < myNumbers[i].length; ++j) {
                System.out.println(myNumbers[i][j]);
            }
        }
    }

    // --------------queue-----------------

    public void linkedList() {
        LinkedList<Integer> ll = new LinkedList<Integer>();

        // add -> appends to end of the list
        // addFirst, addLast

        // get(index), getFirst(), getLast()

        // clear(), contains(o), indexOf, isEmpty

        // peek() -> peeks the head element
        // peekFirst, peekLast

        // poll() -> retrieve and remove the head element
        // pollFirst, pollLast

        // remove() -> removes and returns the first element
        // removeFirst, removeLast

        Iterator<Integer> iterator = ll.iterator();
        while (iterator.hasNext())
            System.out.println(iterator.next());

        ll.forEach(elem -> {
            System.out.println(elem);
        });

        for (Integer ele : ll)
            System.out.println(ele);

    }

    public void stack() {
        LinkedList<Integer> ll = new LinkedList<Integer>();
        ll.push(2);
        ll.pop();

    }

    public void queue() {
        LinkedList<Integer> ll = new LinkedList<Integer>();
        ll.addLast(4);
        ll.removeFirst();
    }

    public void priorityQueue() {

        PriorityQueue<Student> pq = new PriorityQueue<Student>(5, new StudentComparator());
        Student s1 = new Student("A");
        Student s2 = new Student("B");
        Student s3 = new Student("C");
        Student s4 = new Student("D");

        pq.add(s3);
        pq.add(s2);
        pq.add(s4);
        pq.add(s1);

        while (!pq.isEmpty())
            System.out.println(pq.poll().getName());

    }

    public void dequeue() {
        LinkedList<Integer> ll = new LinkedList<Integer>();
        ll.addLast(4);
        ll.addFirst(1);
        ll.removeFirst();
        ll.removeLast();
    }

    // --------------Set-----------------

    public void hashSet() {
        // Unique objects store
        HashSet<Integer> hs = new HashSet<Integer>();
        hs.add(1);
        // clear, contains, isEmpty, remove, size, toArray

        for (Integer x : hs)
            System.out.println(x);

        Iterator<Integer> it = hs.iterator();
        while (it.hasNext())
            System.out.println(it.next());

        hs.forEach((elem) -> {
            System.out.println(elem);
        });
    }

    public void treeSet() {
        // Unique Objects are stored in sorted order
        TreeSet<Integer> ts = new TreeSet<Integer>();
        ts.add(1);
        ts.clear();
        ts.contains(1);
        ts.remove(1);
        ts.size();

        // isEmpty, headSet, tailSet, subset, descendingSet,
        // first, last, lower, floor, ceiling, higher, pollFirst, pollLast

        for (Integer value : ts)
            System.out.print(value + ", ");

        Iterator<Integer> it = ts.iterator();
        while (it.hasNext())
            System.out.print(it.next());

        ts.forEach((elem) -> {
            System.out.println(elem);
        });

        TreeSet<Student> ts_std = new TreeSet<Student>(new StudentComparator());
        ts_std.clear();
    }

    public void linkedHashSet() {
        LinkedHashSet<Integer> lhs = new LinkedHashSet<Integer>();
        // add, clear, clone, contains, equals, isEmpty, remove, size, toArray

        for (Integer value : lhs)
            System.out.print(value + ", ");

        Iterator<Integer> it = lhs.iterator();
        while (it.hasNext())
            System.out.print(it.next());

        lhs.forEach((elem) -> {
            System.out.println(elem);
        });
    }

    // --------------Map-----------------

    public void hashTable() {
        // synchronized and does NOT allow null keys
        // depricated. use concurrentHashMap instead
        Hashtable<Integer, String> ht = new Hashtable<Integer, String>();
        ht.put(1, "a");
        ht.get(1);
        ht.containsKey(1);
        ht.size();

        // clear, clone, containsValue, getOrDefault, isEmpty, keySet,
        // putIfAbsent, remove, replace
        for (Map.Entry<Integer, String> entry : ht.entrySet())
            System.out.println(entry.getKey() + " " + entry.getValue());

        for (Integer key : ht.keySet())
            System.out.println(key + ":" + ht.get(key));

        ht.forEach((key, val) -> {
            ht.replace(key, val, val + "_new");
        });

        Iterator<Map.Entry<Integer, String>> it = ht.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<Integer, String> entry = (Map.Entry<Integer, String>) it.next();
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }

    public void hashMap() {
        // Allows null key/values
        // Not synchronized.
        HashMap<String, String> hm = new HashMap<String, String>();
        hm.put("a", "A");
        hm.get("a");
        hm.clear();
        hm.isEmpty();
        hm.putIfAbsent("a", "A");
        hm.size();
        hm.containsKey("a");

        // remove, replace, containsValue, keySet, getOrDefault, putIfAbsent

        for (Map.Entry<String, String> entry : hm.entrySet())
            System.out.println(entry.getKey() + " " + entry.getValue());

        for (String key : hm.keySet())
            System.out.println(key + ": " + hm.get(key));

        hm.forEach((key, val) -> {
            System.out.println(key + ": " + val);
        });

        Iterator<Map.Entry<String, String>> it = hm.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<String, String> entry = (Map.Entry<String, String>) it.next();
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }

    public void linkedHashMap() {
        LinkedHashMap<String, String> lhm = new LinkedHashMap<String, String>();
        lhm.put("a", "A");
        lhm.get("a");
        lhm.clear();
        lhm.isEmpty();
        lhm.putIfAbsent("a", "A");
        lhm.size();

        // remove, replace, containsValue, keySet, getOrDefault, putIfAbsent
        for (Map.Entry<String, String> entry : lhm.entrySet())
            System.out.println(entry.getKey() + " " + entry.getValue());

        for (String key : lhm.keySet())
            System.out.println(key + ": " + lhm.get(key));

        lhm.forEach((key, val) -> {
            System.out.println(key + ": " + val);
        });

        Iterator<Map.Entry<String, String>> it = lhm.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<String, String> entry = (Map.Entry<String, String>) it.next();
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }

    public void treeMap() {
        // store key/value pairs in sorted order,
        // and allows rapid retrieval
        TreeMap<Integer, String> tm = new TreeMap<Integer, String>();
        tm.put(1, "one");
        tm.get(1);
        tm.isEmpty();
        tm.remove(1);
        tm.replace(1, "ek");
        tm.size();

        // clear, containsKey, containsValue, descendingMap, entrySet, subMap,
        // firstEntry, lastEntry
        // floorEntry, ceilingEntry, higherEntry, lowerEntry, headMap, tailMap,
        // putIfAbsent

        for (Map.Entry<Integer, String> entry : tm.entrySet())
            System.out.println(entry.getKey() + " " + entry.getValue());

        for (Integer key : tm.keySet())
            System.out.println(key + " " + tm.get(key));

        tm.forEach((k, v) -> {
            System.out.println(k + ": " + v);
        });

        Iterator<Map.Entry<Integer, String>> it = tm.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<Integer, String> entry = (Map.Entry<Integer, String>) it.next();
            System.out.println(entry.getKey() + " " + entry.getValue());
        }

        TreeMap<Student, Integer> std_gpa = new TreeMap<Student, Integer>(new StudentComparator());
        std_gpa.clear();
    }

    public void customException() {
        class InvalidAgeException extends Exception {
            InvalidAgeException(String s) {
                super(s);
            }
        }

        class testException {
            void validate(int age) throws InvalidAgeException {
                if (age < 18)
                    throw new InvalidAgeException("You are a minor");
            }
        }

        testException te = new testException();
        try {
            te.validate(23);
        } catch (InvalidAgeException iae) {
            System.out.println(iae.getMessage());
        } finally {
            System.out.println("after check here's what happens");
        }
    }

}