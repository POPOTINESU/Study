package main

func containsDuplicate(nums []int) bool {
	cache := make(map[int]struct{})

	for _, n := range nums {
		if _, ok := cache[n]; ok {
			return true
		}
		cache[n] = struct{}{}
	}
	return false
}
