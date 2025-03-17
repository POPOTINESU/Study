from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = defaultdict(int)
        for c in s:
            cache[c] += 1

        for c in t:
            if cache[c] - 1 < 0:
                return False
            cache[c] -= 1

        return all(v == 0 for v in cache.values())
