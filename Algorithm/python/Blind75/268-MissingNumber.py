from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        expect = size * (size + 1) // 2
        actual = sum(nums)

        return expect - actual
