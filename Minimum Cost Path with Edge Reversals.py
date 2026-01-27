from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        # Build graph
        for u, v, w in edges:
            graph[u].append((v, w))       # normal edge
            graph[v].append((u, 2 * w))   # reversed edge

        INF = float('inf')
        dist = [INF] * n
        dist[0] = 0

        pq = [(0, 0)]  # (cost, node)

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue

            for v, w in graph[u]:
                if dist[v] > cost + w:
                    dist[v] = cost + w
                    heapq.heappush(pq, (dist[v], v))

        return dist[n - 1] if dist[n - 1] != INF else -1
