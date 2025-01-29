'''
@Project : Class
@File : Template.py
@Author : Herbert
@Date : 1/29/2025 10:06 PM
'''
from collections import defaultdict
from collections import deque


def Topological_Sort(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    indegree = [0] * numCourses
    adj = defaultdict(list)
    res = []
    for i, j in prerequisites:
        adj[j].append(i)
        indegree[i] += 1

    q = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        res.append(cur)
        for i in adj[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return res


print(Topological_Sort(6,[[1,0],[1,2],[3,1],[3,2],[2,4],[4,5],[2,5]]))