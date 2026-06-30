'''
@Project : Class
@File : 1976. Number of Ways to Arrive at Destination.py
@Author : Herbert
@Date : 3/23/2025 12:05 PM
'''
import heapq
from collections import defaultdict


class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        for a, b, c in roads:
            adj[a].append((c, b))
            adj[b].append((c, a))

        pq = [(0, 0)]
        ways = [0] * n
        dist = [float('inf')] * n
        ways[0] = 1
        dist[0] = 0
        MOD = 10 ** 9 + 7

        while pq:
            cost, node = heapq.heappop(pq)
            if cost > dist[node]:
                continue
            for c, nei in adj[node]:
                new_cost = c + cost
                if dist[nei] > new_cost:
                    dist[nei] = new_cost
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_cost, nei))
                elif dist[nei] == new_cost:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        return ways[n - 1]