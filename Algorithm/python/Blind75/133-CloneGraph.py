from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        visited = {}

        def dfs(node: Node):
            if node in visited:
                return visited[node]
            clone = Node(node.val)
            visited[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)

    def bfsCloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        visited: dict[Node, Node] = {}
        queue = deque([node])
        visited[node] = Node(node.val)

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    clone = Node(neighbor.val)
                    visited[neighbor] = clone
                    queue.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])

        return visited[node]
