class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return size
        result = 0

        def count_palindromes(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < size and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        for i in range(size):
            result += count_palindromes(i, i) + count_palindromes(i, i + 1)

        return result
