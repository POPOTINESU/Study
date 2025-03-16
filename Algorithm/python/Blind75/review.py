class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_length = len(s)
        if s_length < 2:
            return s_length

        left = 0
        longest = 1
        visited = {}

        for right in range(s_length):
            if s[right] in visited and visited[s[right]] >= left:
                left = visited[s[right]] + 1

            visited[s[right]] = right
            longest = max(longest, right - left + 1)

        return longest
