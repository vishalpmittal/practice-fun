package ocpjp.examples;

import java.util.ArrayList;
import java.util.List;

public class Test {

    public static void main(String[] args) {
        List<String> myList = new ArrayList<String>();
        populateList(myList);
        String str = myList.get(2);

    }

    public static void populateList(List<String> list) {
        list.add("abc");
        // list.add(34);
        // list.add(new Student("a", 3));
    }
}
