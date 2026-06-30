'''
@Project : Class
@File : Directed.py
@Author : Herbert
@Date : 2/16/2024 10:25 PM
'''
from collections import defaultdict


def detect_cycle_in_directed_graph(edges, n):
    graph = defaultdict(list)
    for n1, n2 in edges:
        graph[n1].append(n2)

    visited = [False] * n
    path = [False] * n

    def dfs(cur, visited, path):
        visited[cur] = True
        path[cur] = True

        for node in graph[cur]:
            if not visited[node]:
                if dfs(node, visited, path):
                    return True
            elif path[node]:
                return True

        path[cur] = False
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i, visited, path):
                return True
    return False


print(detect_cycle_in_directed_graph(edges=[(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)], n=4))
