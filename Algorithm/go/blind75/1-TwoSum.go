package main

/*
search one pair that they add up to target.
*/
func twoSum(nums []int, target int) []int {
	cache := map[int]int{}

	for i, n := range nums {
		diff := target - n
		if cacheIndex, ok := cache[diff]; ok {
			return []int{cacheIndex, i}
		}
		cache[n] = i
	}

	return nil //cannot find pair
}

// func main() {
// 	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
// }
