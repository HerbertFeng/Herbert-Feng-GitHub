'''
@Project : Class
@File : 2685. Count the Number of Complete Components.py
@Author : Herbert
@Date : 3/22/2025 10:35 PM
'''
from collections import defaultdict


class Solution:
    def countCompleteComponents_dfs(self, n: int, edges: List[List[int]]) -> int:
        # DFS
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        res = 0
        vis = set()

        def dfs(cur):
            vis.add(cur)
            vertex = 1
            edge = len(adj[cur])
            for i in adj[cur]:
                if i not in vis:
                    v, e = dfs(i)
                    vertex += v
                    edge += e
            return vertex, edge

        for i in range(n):
            if i not in vis:
                V, E = dfs(i)
                if V * (V - 1) == E:  # since the edges are double counted
                    res += 1
        return res

    def countCompleteComponents_DSU(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        dsu = DSU(n)
        edge_count = defaultdict(int)
        for n1, n2 in edges:
            dsu.union(n1, n2)

        for e1, e2 in edges:
            root = dsu.find(e1)
            edge_count[root] += 1

        res = 0
        for v in range(n):
            if dsu.find(v) == v:
                node_count = dsu.size[v]
                expected_edge = (node_count * (node_count - 1)) // 2
                if expected_edge == edge_count[v]: res += 1

        return res


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.size[p1] < self.size[p2]:
            p1, p2 = p2, p1
        self.parent[p2] = p1
        self.size[p1] += self.size[p2]
        return True
