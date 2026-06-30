'''
@Project : Class
@File : Undirected.py
@Author : Herbert
@Date : 2/16/2024 10:43 PM
'''

from collections import defaultdict


def detect_cycle_in_undirected_graph(edges, n):
    graph = defaultdict(list)
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    visited = [False] * n

    def dfs(cur, visited, last):
        visited[cur] = True

        for node in graph[cur]:
            if not visited[node]:
                if dfs(node, visited, cur):
                    return True
            elif last != node:
                return True
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i, visited, -1):
                return True
    return False


print(detect_cycle_in_undirected_graph([(1, 0), (1, 2), (2, 0), (0, 3), (3, 4)], 5))
