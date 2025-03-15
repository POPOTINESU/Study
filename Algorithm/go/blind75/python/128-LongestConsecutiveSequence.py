from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 1
        nums_set = set(nums)
        
        for num in nums:
            # Find start point of consecutive nums
            if num -1 not in nums_set:
                count = 1
                
                # Count consecutive nums
                while num + 1 in nums_set:
                    count += 1
                    num += 1

                longest = max(longest, count)

        return longest