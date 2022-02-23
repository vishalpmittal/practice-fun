/**
 * Design a BrowserHistory class:
 * - initialize with a base url 
 * - visit(url) takes you to specified url
 * - back(n) takes to n step back
 * - forward(n) takes you n step forward
 * 
 * eg: 
 * browserhistory(google.com)
 * visit(facebook.com) g -> f
 * back(1) g -> f
 * forward(1) g -> f
 * visit(amazon.com) g -> f -> a
 * back(2) g -> f -> a
 * visit(newegg.com) g -> newegg
 * forward(1)
 * 
 */

package dsAlgo.list;

import static org.junit.Assert.assertTrue;

import java.io.*;
import java.util.*;

public class BrowserHistory {
    LinkedList<String> curr_visits;
    LinkedList<String> prev_visits;

    public BrowserHistory(String homepage) {
        curr_visits = new LinkedList<String>();
        prev_visits = new LinkedList<String>();
        curr_visits.push(homepage);
    }

    public String get_current() {
        return curr_visits.peek();
    }

    public void visit(String url) {
        prev_visits = new LinkedList<String>();
        curr_visits.push(url);
    }

    public String back(int steps) {
        int i = 0;
        while (curr_visits.size() > 1 && i < steps) {
            prev_visits.push(curr_visits.pop());
            i++;
        }
        return this.get_current();
    }

    public String forward(int steps) {
        int i = 0;
        while (prev_visits.size() > 0 && i < steps) {
            curr_visits.push(prev_visits.pop());
            i++;
        }
        return this.get_current();
    }
}

class Solution {
    public static void main(String[] args) {
        BrowserHistory bh = new BrowserHistory("g");
        assertTrue(bh.get_current().equals("g"));
        bh.visit("f");
        assertTrue(bh.get_current().equals("f"));
        bh.visit("a");
        assertTrue(bh.get_current().equals("a"));
        assertTrue(bh.back(1).equals("f"));
        assertTrue(bh.forward(1).equals("a"));
        assertTrue(bh.back(2).equals("g"));

        bh.visit("n");
        assertTrue(bh.get_current().equals("n"));
        assertTrue(bh.forward(5).equals("n"));
        assertTrue(bh.back(6).equals("g"));
        System.out.println("Tests Passed!!!");
    }
}
