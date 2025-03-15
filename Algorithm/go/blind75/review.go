package main

func review(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	// Build the cache
	cache := make(map[rune]int)
	for _, r := range s {
		cache[r]++
	}

	// Check for anagram
	for _, r := range t {
		if n, ok := cache[r]; ok {
			if n-1 < 0 {
				return false
			}
			cache[r] = n - 1
		} else {
			return false
		}
	}

	return true
}
