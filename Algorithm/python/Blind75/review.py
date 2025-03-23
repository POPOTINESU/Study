from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self._parent = list(range(n)) 
        self._rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        if x != self._parent[x]:
            x = self.find(self._parent[x])
        return self._parent[x]

    def union(self, x: int, y: int) -> bool:
        X_root = self.find(x)
        Y_root = self.find(y)

        if X_root == Y_root:
            return False

        if self._rank[X_root] > self._rank[Y_root]:
            self._parent[Y_root] = X_root
        elif self._rank[X_root] < self._rank[Y_root]:
            self._parent[X_root] = Y_root
        else:
            self._parent[Y_root] = X_root
            self._rank[X_root] += 1

        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        union_find = UnionFind(n)
        
        for x, y in edges:
            if not union_find.union(x, y):
                return False
        
        return True

if __name__ == "__main__":
    s = Solution()

    print(s.validTree(5,[[0,1],[0,2],[0,3],[1,4]]))