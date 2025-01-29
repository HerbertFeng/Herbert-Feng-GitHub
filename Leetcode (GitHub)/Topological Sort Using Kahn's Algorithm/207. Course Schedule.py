'''
@Project : Class
@File : 207. Course Schedule.py
@Author : Herbert
@Date : 1/29/2025 10:05 PM
'''
from collections import defaultdict
from collections import deque


def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    indegree = [0] * numCourses
    adj = defaultdict(list)
    for i, j in prerequisites:
        adj[j].append(i)
        indegree[i] += 1

    q = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        for i in adj[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return sum(indegree) == 0
