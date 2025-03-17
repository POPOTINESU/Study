class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 1:
            return len(s)

        def count_palindromic_substrings(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        result = 0
        for i in range(len(s)):
            result += count_palindromic_substrings(i, i)
            result += count_palindromic_substrings(i, i + 1)
        
        return result
