'''
@Project : Class
@File : 802. Find Eventual Safe States.py
@Author : Herbert
@Date : 1/29/2025 10:02 PM
'''

from collections import deque
def eventualSafeNodes(graph):  # detect nodes with cycles
    """
    :type graph: List[List[int]]
    :rtype: List[int]
    """
    # Topological Sort Using Kahn's Algorithm
    # https://www.youtube.com/watch?v=cIBFEhD77b4
    n = len(graph)
    indegree = [0] * n
    adj = [[] for _ in range(n)]  # flip the dir of arrow in 'graph' from outdegree to indegree

    for i in range(n):
        for node in graph[i]:
            adj[node].append(i)
            indegree[i] += 1


    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    safe = [False] * n
    while q:
        node = q.popleft()
        safe[node] = True
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    safeNode = []
    for i in range(n):
        if safe[i]:
            safeNode.append(i)
    return safeNode
