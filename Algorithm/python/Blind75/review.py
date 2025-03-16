from collections import defaultdict, deque
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # Create adjacency list
        graph_map = defaultdict(list)
        for a, b in edges:
            graph_map[a].append(b)
            graph_map[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph_map[node]:
                dfs(neighbor)

        dfs(0)
        return len(visited) == n
