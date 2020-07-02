package dsAlgo;

import java.util.concurrent.ArrayBlockingQueue;

import java.util.concurrent.ConcurrentHashMap;

import java.util.concurrent.ConcurrentLinkedDeque;
import java.util.concurrent.ConcurrentLinkedQueue;

import java.util.concurrent.ConcurrentSkipListMap;
import java.util.concurrent.ConcurrentSkipListSet;

import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.CopyOnWriteArraySet;

import java.util.concurrent.DelayQueue;

import java.util.concurrent.LinkedBlockingDeque;
import java.util.concurrent.LinkedTransferQueue;
import java.util.concurrent.LinkedBlockingQueue;

import java.util.concurrent.PriorityBlockingQueue;

import java.util.concurrent.SynchronousQueue;

import java.util.Map;
import java.util.Iterator;

public class DataStructures_concurrent {

    public static void concurrentHashMap() {
        // underlined data structure is Hashtable
        // is thread-safe
        // Default concurrency-level of ConcurrentHashMap is 16
        // null insertion is not possible in ConcurrentHashMap as key or value.

        ConcurrentHashMap<String, String> hm = new ConcurrentHashMap<String, String>();
        hm.put("a", "A");
        hm.get("a");
        hm.clear();
        hm.isEmpty();
        hm.putIfAbsent("a", "A");
        hm.size();

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
}