'''
@Project : Class
@File : 2368. Reachable Nodes With Restrictions (Medium).py
@Author : Herbert
@Date : 2/8/2024 2:02 PM
'''
from collections import defaultdict


class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        res = set(restricted)
        graph = defaultdict(list)
        vis = set()

        for u, v in edges:
            if u in res or v in res:
                continue
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            r = 1
            for nei in graph[node]:
                if nei in vis:
                    continue
                vis.add(nei)
                r += dfs(nei)
            return r

        vis.add(0)
        return dfs(0)
