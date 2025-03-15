class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        cache = dict()
        longest = 1
        s_length = len(s)
        for i in range(s_length):
            right = i + 1
            count = 1
            while right < s_length:
                hit = cache.get(s[right])
                if hit and hit >= 1:
                    longest = max(longest, count)
                    break

                count += 1
                right += 1

        return longest

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))