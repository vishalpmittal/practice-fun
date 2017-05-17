package dsAlgo.todo;

import java.util.TreeSet;

public class CountSortedTreeSet {
    TreeSet<CSortedElement> cSTreeSet = null;

    public CountSortedTreeSet() {
        this.cSTreeSet = new TreeSet<CSortedElement>();
    }

    public void addElement(String s) {
        if (this.cSTreeSet.contains(new CSortedElement(s))) {
        }

    }

}

class CSortedElement implements Comparable {
    private String elem;
    private int count;

    public CSortedElement(String elem) {
        this.elem = elem;
        this.count = 1;
    }

    public String getElem() {
        return elem;
    }

    public void setElem(String elem) {
        this.elem = elem;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof CSortedElement) {
            CSortedElement cse = (CSortedElement) obj;
            return this.getElem().equals(cse.getElem());
        } else
            return false;
    }

    @Override
    public int compareTo(Object o) {
        if (!(o instanceof CSortedElement)) {
            return -1;
        }

        CSortedElement cse = (CSortedElement) o;
        return Integer.compare(this.count, cse.count);
    }

}
