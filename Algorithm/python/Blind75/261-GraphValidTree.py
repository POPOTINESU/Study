from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self._parent = [i for i in range(n)]
        self._rank = [1] * n

    def find(self, x: int) -> int:
        if x != self._parent[x]:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]

    def union(self, edge1: int, edge2: int) -> int:
        rootX = self.find(edge1)
        rootY = self.find(edge2)

        if rootX == rootY:
            return False

        if self._rank[rootX] > self._rank[rootY]:
            self._parent[rootY] = rootX
        elif self._rank[rootX] < self._rank[rootY]:
            self._parent[rootX] = rootY
        else:
            self._parent[rootY] = rootX
            self._rank[rootX] += 1

        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        union_find = UnionFind(n)
        for edge1, edge2 in edges:
            if not union_find.union(edge1, edge2):
                return False

        return True
