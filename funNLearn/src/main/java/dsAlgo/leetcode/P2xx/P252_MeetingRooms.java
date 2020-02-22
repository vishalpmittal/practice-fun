/**
 * Tag: array
 * 
 * Given an array of meeting time intervals consisting of start and end times 
 * [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
 * 
 * For example,
 * Given [[0, 30],[5, 10],[15, 20]],
 * return false.
 */

package dsAlgo.leetcode.P2xx;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;
import java.util.Comparator;

import dsAlgo.leetcode.dependencies.Interval;

public class P252_MeetingRooms {
	public static boolean canAttendMeetings(Interval[] intervals) {
		if (intervals == null)
			return false;

		// Sort the intervals by start time
		Arrays.sort(intervals, new Comparator<Interval>() {
			public int compare(Interval a, Interval b) {
				return a.start - b.start;
			}
		});

		for (int i = 1; i < intervals.length; i++)
			if (intervals[i].start < intervals[i - 1].end)
				return false;

		return true;
	}

	public static void main(String[] args) {
		Interval i1 = new Interval(0, 30);
		Interval i2 = new Interval(5, 10);
		Interval i3 = new Interval(15, 20);
		Interval i4 = new Interval(0, 4);
		Interval[] arr = { i1, i2, i3 };
		Interval[] arr1 = { i4, i2, i3 };

		assertTrue("Test1", canAttendMeetings(arr1));
		assertFalse("Test2", canAttendMeetings(arr));
		System.out.println("All Tests passed");
	}
}
