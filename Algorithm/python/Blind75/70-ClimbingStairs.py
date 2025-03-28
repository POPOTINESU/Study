class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
