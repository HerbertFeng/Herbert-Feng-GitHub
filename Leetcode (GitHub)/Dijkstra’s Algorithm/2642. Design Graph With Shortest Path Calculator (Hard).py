'''
@Project : Class
@File : 2642. Design Graph With Shortest Path Calculator (Hard).py
@Author : Herbert
@Date : 2/14/2024 1:41 PM
'''

import heapq


class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        self.graph = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            self.graph[i][j] = w

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        self.graph[edge[0]][edge[1]] = edge[2]

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        n = len(self.graph)
        distance = [float('inf')] * n
        distance[node1] = 0
        visited = set()
        heap = [(0, node1)]
        while heap:
            cur_cost, cur_node = heapq.heappop(heap)

            if cur_node == node2:
                return cur_cost
            if cur_node in visited:
                continue

            visited.add(cur_node)
            for neighbor, cost in enumerate(self.graph[cur_node]):
                if distance[neighbor] > cur_cost + cost:
                    distance[neighbor] = cur_cost + cost
                    heapq.heappush(heap, (int(cur_cost + cost), neighbor))

        return -1
