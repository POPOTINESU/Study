package main

func review(nums []int) int {
	size := len(nums)
	expect := size * (size + 1) / 2
	actual := 0

	for _, n := range nums {
		actual += n
	}

	return expect - actual
}
