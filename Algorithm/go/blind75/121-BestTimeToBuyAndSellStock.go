package main

func maxProfit(prices []int) int {
	// Cannot buy and sell on the same day
	if len(prices) < 2 {
		return 0
	}

	minPrice := prices[0]
	maxProfit := 0

	for _, price := range prices {
		if price < minPrice {
			minPrice = price
		}

		// Calculate profit based on current price
		profit := price - minPrice

		if profit > maxProfit {
			maxProfit = profit
		}
	}
	return maxProfit
}
