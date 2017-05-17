/*
 * Input: You are given data where each user has their favorite food items.
 * UA -> [F1, F2, F3, F4, F5, F20]
 * UB -> [F3, F10, F20, F200]
 * UC -> [F2, F3, F4, F300]
 * UD -> [F20, F200]
 * UE -> [F300]
 * UF -> [F400]
 *  
 * Output: Return a sorted relationship of users with other users based on their favorites
 * UA -> [UC, UB, UD]
 * UB -> [UD, UA, UC]
 * UC -> [UA, UB, UE]
 * UD -> [UB, UA] 
 * UE -> [UC]
 * UF -> []
 */

package dsAlgo.todo;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

public class UserRelationships {
    private static HashMap<String, HashSet<String>> userFavs = new HashMap<String, HashSet<String>>();

    private static void populateTestData() {
        HashSet<String> tempList = new HashSet<String>(Arrays.asList("F1", "F2", "F3", "F4", "F5", "F20"));
        userFavs.put("UA", tempList);

        tempList = new HashSet<String>(Arrays.asList("F3", "F10", "F20", "F200"));
        userFavs.put("UB", tempList);

        tempList = new HashSet<String>(Arrays.asList("F2", "F3", "F4", "F300"));
        userFavs.put("UC", tempList);

        tempList = new HashSet<String>(Arrays.asList("F20", "F200"));
        userFavs.put("UD", tempList);

        tempList = new HashSet<String>(Arrays.asList("F300"));
        userFavs.put("UE", tempList);

        tempList = new HashSet<String>(Arrays.asList("F400"));
        userFavs.put("UF", tempList);
    }

    private static void printHashMapOfStringNList(HashMap<String, HashSet<String>> hmOfStrHashSet) {
        System.out.println("--------------------");
        for (String key : hmOfStrHashSet.keySet()) {
            System.out.println(key + "->" + hmOfStrHashSet.get(key).toString());
        }
        System.out.println("--------------------");
    }

    private static HashMap<String, HashMap<String, Integer>> getUserRelations() {
        HashMap<String, HashSet<String>> foodToUsersMap = new HashMap<String, HashSet<String>>();
        HashMap<String, HashMap<String, Integer>> userRelations = new HashMap<String, HashMap<String, Integer>>();

        for (String user : userFavs.keySet()) {
            userRelations.put(user, new HashMap<String, Integer>());
        }

        for (String user : userFavs.keySet()) {
            Set<String> userFavSet = userFavs.get(user);

            for (String food : userFavSet) {
                if (!foodToUsersMap.containsKey(food)) {
                    foodToUsersMap.put(food, new HashSet<String>());
                }
                foodToUsersMap.get(food).add(user);

                if (foodToUsersMap.get(food).size() < 2)
                    continue;

                for (String connUser : foodToUsersMap.get(food)) {
                    if (user.compareTo(connUser) == 0)
                        continue;

                    if (!userRelations.get(user).containsKey(connUser)) {
                        userRelations.get(user).put(connUser, 0);
                    }
                    userRelations.get(user).put(connUser, (userRelations.get(user).get(connUser)) + 1);

                    if (!userRelations.get(connUser).containsKey(user)) {
                        userRelations.get(connUser).put(user, 0);
                    }
                    userRelations.get(connUser).put(user, (userRelations.get(connUser).get(user)) + 1);
                }
            }
        }

        printHashMapOfStringNList(foodToUsersMap);
        return userRelations;
    }

    private static void printUserRaltions(HashMap<String, HashMap<String, Integer>> userRelations) {
        Comparator<Entry<String, Integer>> valueComparator = new Comparator<Entry<String, Integer>>() {
            @Override
            public int compare(Entry<String, Integer> e1, Entry<String, Integer> e2) {
                return Integer.compare(e1.getValue(), e2.getValue());
            }
        };

        // String[] keysArray = userRelations.keySet().toArray(new String[0]);
        // Arrays.sort(keysArray);
        System.out.println();
        for (String key : userRelations.keySet()) {
            Set<String> rel = userRelations.get(key).keySet();
            TreeSet<String> ts = new TreeSet<String>(rel) {
                
                
            };
            
            
            
            List<Entry<String, Integer>> relations = new ArrayList<Entry<String, Integer>>(
                    (Collection<? extends Entry<String, Integer>>) userRelations.get(key));

            Collections.sort(relations, valueComparator);

            System.out.println(key + "->");
            System.out.println(relations.toString());
        }
    }

    public static void main(String[] args) {
        populateTestData();
        printHashMapOfStringNList(userFavs);
        printUserRaltions(getUserRelations());
    }
}