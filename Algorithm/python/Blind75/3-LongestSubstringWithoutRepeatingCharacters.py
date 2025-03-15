class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        longest = 0

        # Use sliding window algorithm
        left = 0
        for right in range(len(s)):
            if s[right] in cache and cache[s[right]] >= left:
                left = cache[s[right]] + 1

            cache[s[right]] = right
            longest = max(longest, right - left + 1)

        return longest


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
