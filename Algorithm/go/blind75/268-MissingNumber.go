package main

func missingNumber(nums []int) int {
	size := len(nums)

	// use theorem of gauss
	expect := size * (size + 1) / 2
	actual := 0

	for _, n := range nums {
		actual += n
	}
	return expect - actual
}

// func main() {
// 	missingNumber([]int{3, 0, 1})
// }
