package main

import "sort"

func canAttendMeetings(intervals [][]int) bool {
	if len(intervals) < 2 {
		return true
	}
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	for i := 0; i < len(intervals)-1; i++ {
		if intervals[i+1][0] < intervals[i][1] {
			return false
		}
	}
	return true
}
