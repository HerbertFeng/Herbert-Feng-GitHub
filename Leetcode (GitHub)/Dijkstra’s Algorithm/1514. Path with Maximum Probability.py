'''
@Project : Class
@File : 1514. Path with Maximum Probability.py
@Author : Herbert
@Date : 2/15/2024 4:28 PM
'''
import heapq
from collections import defaultdict


def maxProbability(n, edges, succProb, start_node, end_node):
    """
    :type n: int
    :type edges: List[List[int]]
    :type succProb: List[float]
    :type start_node: int
    :type end_node: int
    :rtype: float
    """
    p = [0.0] * n
    adj = defaultdict(list)
    for i in range(len(edges)):
        adj[edges[i][0]].append((succProb[i], edges[i][1]))
        adj[edges[i][1]].append((succProb[i], edges[i][0]))

    p[start_node] = 1.0
    heap = [(-p[start_node], start_node)]
    while heap:
        prob, cur = heapq.heappop(heap)
        if cur == end_node:
            return -prob
        for p1, node1 in adj[cur]:
            if p[node1] < -prob * p1:
                p[node1] = -prob * p1
                heapq.heappush(heap, (-p[node1], node1))
    return 0.0