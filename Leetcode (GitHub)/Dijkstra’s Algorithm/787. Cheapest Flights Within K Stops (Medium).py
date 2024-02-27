'''
@Project : Class
@File : 787. Cheapest Flights Within K Stops (Medium).py
@Author : Herbert
@Date : 2/25/2024 1:05 PM
'''
import heapq
from collections import defaultdict


def findCheapestPrice(n, flights, src, dst, k):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type k: int
    :rtype: int
    """
    adj = defaultdict(list)
    for a, b, c in flights:
        adj[a].append((c, b))

    minHeap = []
    dist = [float('inf')] * n
    stops = [float('inf')] * n

    dist[src] = 0
    stops[src] = 0
    heapq.heappush(minHeap, (0, src, 0))

    while minHeap:
        curDist, curNode, curStops = heapq.heappop(minHeap)
        if curNode == dst:
            return curDist
        if curStops == k + 1:
            continue
        for nextWeight, nextNode in adj[curNode]:
            nextDist = curDist + nextWeight
            nextStops = curStops + 1
            if nextDist < dist[nextNode] or nextStops < stops[nextNode]:
                dist[nextNode] = nextDist
                stops[nextNode] = nextStops
                heapq.heappush(minHeap, (nextDist, nextNode, nextStops))

    return -1

'''
@cache
def dfs(node,k):
    if node == 1:
        return 0
    if k==-1:
        return float('inf')

    dis = float('inf')
    for f,p in dic[node]:
        dis = min(dfs(f,k-1)+p,dis)
    return dis
'''