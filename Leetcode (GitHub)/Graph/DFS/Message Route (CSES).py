'''
@Project : Class
@File : Message Route (CSES).py
@Author : Herbert
@Date : 2/28/2025 10:42 PM
'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

'''
5 5
1 2
1 3
1 4
2 3
5 4
'''
def solve():
    n,m = map(int,input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    dq = deque([1])
    dist = [-1]*(n+1)
    dist[1]=0
    parent = [-1]*(n+1)

    while dq:
        node = dq.popleft()
        for i in graph[node]:
            if dist[i]==-1:
                dist[i] = dist[node]+1
                parent[i] = node
                dq.append(i)
                if i==n:
                    path = []
                    cur = n
                    while cur!=-1:
                        path.append(cur)
                        cur = parent[cur]
                    path.reverse()
                    print(len(path))
                    print(' '.join(map(str,path)))
                    return
    print('IMPOSSIBLE')
    return

solve()