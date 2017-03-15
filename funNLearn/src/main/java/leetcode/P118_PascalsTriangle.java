/*
* Given numRows, generate the first numRows of Pascal's triangle.
* 
* For example, given numRows = 5,
* Return
* 
* [
*      [1],
*     [1,1],
*    [1,2,1],
*   [1,3,3,1],
*  [1,4,6,4,1]
* ]
*/

package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class P118_PascalsTriangle {

	public static List<List<Integer>> generate(int numRows) {
		List<List<Integer>> listOfList = new ArrayList<List<Integer>>();
		if (numRows == 0)
			return listOfList;

		listOfList.add(new ArrayList<Integer>(Arrays.asList(1)));
		List<Integer> listn, pre = null;
		for (int row = 2; row <= numRows; row++) {
			listn = new ArrayList<Integer>(Arrays.asList(1));
			for (int n = 1; n < row - 1; n++) {
				listn.add(pre.get(n - 1) + pre.get(n));
			}
			listn.add(1);
			pre = listn;
			listOfList.add(listn);
		}
		return listOfList;
	}

	public static void main(String[] args) {
		// [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
		System.out.println(generate(5));
	}
}
