package main

func review(n int) int {
	result := 0

	for n > 0 {
		n = n & (n - 1)
		result ++
	}
	return result
}
