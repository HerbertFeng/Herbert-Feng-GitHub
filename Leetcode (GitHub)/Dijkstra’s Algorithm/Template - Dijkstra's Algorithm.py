'''
@Project : Class
@File : Template - Dijkstra's Algorithm.py
@Author : Herbert
@Date : 2/15/2024 5:30 PM
'''

import heapq
from collections import defaultdict


def shortestPath(n, edges, start, end):
    adj = defaultdict(list)
    for n1, n2, w in edges:
        adj[n1].append((n2, w))

    distance = [float('inf')] * n
    distance[start] = 0

    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)

        if node == end:
            return cost

        for n2, cur_cost in adj[node]:
            if distance[n2] > cur_cost + cost:
                distance[n2] = cur_cost + cost
                heapq.heappush(heap, (cur_cost + cost, n2))

    return -1


print(shortestPath(5, edges=[[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]], start=0, end=4))
