from typing import List


class UnionFind:
    def __init__(self, n: int):
        self._parent = [i for i in range(n)]
        self._rank = [1] * n

    def find(self, edge: int):
        if edge != self._parent[edge]:
            self._parent[edge] = self.find(self._parent[edge])

        return self._parent[edge]

    def union(self, edge1: int, edge2: int):
        edgeX = self.find(edge1)
        edgeY = self.find(edge2)

        if edgeX == edgeY:
            return False

        if self._rank[edgeX] > self._rank[edgeY]:
            self._parent[edgeY] = edgeX
        elif self._rank[edgeX] < self._rank[edgeY]:
            self._parent[edgeX] = edgeY
        else:
            self._parent[edgeY] = edgeX
            self._rank[edgeX] += 1

        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        unionFind = UnionFind(n)

        for A, B in edges:
            if not unionFind.union(A, B):
                return False

        return True
