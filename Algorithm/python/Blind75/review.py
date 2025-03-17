from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for right in range(1, len(s) + 1):
            for left in range(right):
                if dp[left] and s[left:right] in word_set:
                    dp[right] = True
                    break
        
        return dp[len(s)]