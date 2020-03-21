package dsAlgo.list;

import java.util.Collections;
import java.util.PriorityQueue;

public class KthSmallestElement {

	/*
	 * use a maxHeap data structure
	 * O(n log(k))
	 */
	public static int kthSmallestViaHeap(int[] array, int k) {
		if (k <= 0 || k > array.length) {
			throw new IllegalArgumentException();
		}

		PriorityQueue<Integer> smallestK = new PriorityQueue<Integer>(k, Collections.reverseOrder());
		for (int i = 0; i < k; i++) {
			smallestK.add(array[i]);
		}

		for (int j = k; j < array.length; j++) {
			if (array[j] < smallestK.peek()) {
				smallestK.remove();
				smallestK.add(array[j]);
			}
		}
		return smallestK.peek();
	}

	/*
	 * use a maxHeap data structure
	 * O(n)
	 */
	public static int kthSmallestSelectionRank(int[] array, int k) {
		if (k <= 0 || k > array.length) {
			throw new IllegalArgumentException();
		}
		return elementRank(array, 0, (array.length)-1, k-1);
	}
	
	private static int elementRank(int[] array, int left, int right, int k){
//		int pivotIndex = left + rand.nextInt(right+1-left);
//		int pivot = array[pivotIndex];
//		
//		int sizeSmall = compareToPivot(array, left, right, pivot) - left +1;
//		if (sizeSmall -1 == k){
//			return pivot;
//		}
//		else if (sizeSmall > k){
//			return elementRank(array, left, left+sizeSmall-1, k);
//		}
//		else{
//			return elementRank(array, left+sizeSmall, right, k-sizeSmall);
//		}
		return -1;
	}
	
	
	
	public static void main(String[] args) {
		int [] testarr = {17, 42, 0, 5, 10, -3, 2, 9};
		System.out.println(kthSmallestViaHeap(testarr, 3));
	}

}
