'''
@Project : Class
@File : Longest Flight Route (CSES).py
@Author : Herbert
@Date : 2/23/2025 1:31 AM
'''
from collections import defaultdict, deque


# longest path in a DAG


def solve():
    n, m = map(int, input().split())
    indegree = [0] * n
    res = []
    dq = deque()
    adj = defaultdict(list)
    back = defaultdict(list)  # store the reversed edge for tracking back the prevous node later on
    for _ in range(m):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        adj[a].append(b)
        back[b].append(a)
        indegree[b] += 1

    for i in range(n):
        if indegree[i] == 0:
            dq.append(i)

    while dq:
        cur = dq.popleft()
        for ele in adj[cur]:
            indegree[ele] -= 1
            if indegree[ele] == 0:
                dq.append(ele)
        res.append(cur)

    parent = [-1] * n
    dist = [-float('inf')] * n  # max distance from 1 to i
    dist[0] = 1
    for i in range(n):
        node = res[i]
        for prev in back[node]:
            if dist[prev] + 1 > dist[node]:
                dist[node] = dist[prev] + 1
                parent[node] = prev

    if dist[n - 1] == - float('inf'):
        print('IMPOSSIBLE')
    else:
        print(dist[n - 1])
        # from the end, trace backward
        at = n - 1
        route = []
        while parent[at] != -1:
            route.append(at)
            at = parent[at]
        route.append(0)
        print(*[c + 1 for c in route[::-1]])


solve()

'''
5 5
1 2
2 5
1 3
3 4
4 5
'''