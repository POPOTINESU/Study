package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	cache := make(map[rune]int)
	for _, r := range s {
		cache[r]++
	}

	for _, r := range t {
		if v, ok := cache[r]; ok {
			if v-1 < 0 {
				return false
			}
			cache[r] = v - 1
		} else {
			return false
		}
	}

	for _, v := range cache {
		if v != 0 {
			return false
		}
	}

	return true
}
