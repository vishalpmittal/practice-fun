/*
 * Given an index k, return the kth row of the Pascal's triangle.
 * 
 * For example, given k = 3,
 * Return [1,3,3,1].
 * 
 * Note:
 * Could you optimize your algorithm to use only O(k) extra space?
 */

package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class P119_PascalsTriangleII {
	public static List<Integer> getRow(int rowIndex) {
		List<Integer> pre = new ArrayList<Integer>();
		pre.add(1);
		if (rowIndex == 0)
			return pre;
		pre.add(1);

		List<Integer> listn = null;
		for (int row = 2; row <= rowIndex; row++) {
			listn = new ArrayList<Integer>(Arrays.asList(1));
			for (int n = 1; n < row; n++) {
				listn.add(pre.get(n - 1) + pre.get(n));
			}
			listn.add(1);
			pre = listn;
		}
		return pre;
	}

	/*
	 * More Efficient Solution
	 * We use the same list to save and reset the values
	 */
	public static List<Integer> getRow_1(int rowIndex) {
		List<Integer> list = new ArrayList<Integer>();
		if (rowIndex < 0)
			return list;

		for (int i = 0; i < rowIndex + 1; i++) {
			list.add(0, 1);
			for (int j = 1; j < list.size() - 1; j++) {
				list.set(j, list.get(j) + list.get(j + 1));
			}
		}
		return list;
	}

	public static void main(String[] args) {
		// [1, 4, 6, 4, 1]
		System.out.println(getRow_1(4));
	}
}
