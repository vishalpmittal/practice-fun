package javaMisc;

import java.util.ArrayList;
import java.util.List;

class ListCreator {
    public <T> List<T> createList(T[] strArray) {
        List<T> strList = new ArrayList<T>();
        for (T str : strArray) {
            strList.add(str);
        }
        return strList;
    }

}

public class GenericMethodsSample {
    public static void main(String[] args) {
        String[] strArray = { "a", "b", "c", "d", "e" };
        Integer[] intArray = { 1, 2, 3, 4, 5, 6, 7, 8 };

        ListCreator lc1 = new ListCreator();
        List<String> myList1 = lc1.createList(strArray);

        ListCreator lc2 = new ListCreator();
        List<Integer> myList2 = lc2.createList(intArray);

        System.out.println(myList1);
        System.out.println(myList2);

    }
}
