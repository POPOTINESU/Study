from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_size = 0

        while left < right:
            low_h = min(height[left], height[right])
            max_size = max(max_size, low_h * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_size
