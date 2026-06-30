'''
@Project : Class
@File : Building Roads (CSES).py
@Author : Herbert
@Date : 2/24/2025 1:32 PM
'''

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
'''
4 2
1 2
3 4
'''
'''
#DFS
n,m = map(int,input().split())
visited = [False]*n
adj = [[] for _ in range(n)]
rep = []


for _ in range(m):
    a,b= map(int,input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

def dfs(i):
    visited[i]=True
    for x in adj[i]:
        if not visited[x]:
            dfs(x)

for i in range(n):
    if not visited[i]:
        dfs(i)
        rep.append(i)
print(len(rep)-1)
for i in range(1,len(rep)):
    print(rep[i-1]+1,rep[i]+1)
'''
# BFS

n, m = map(int, input().split())
visited = [False] * n
adj = [[] for _ in range(n)]
rep = []

for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)


def BFS(i):
    dq = deque([i])
    while dq:
        cur = dq.popleft()

        for x in adj[cur]:
            if not visited[x]:
                visited[x] = True
                # mark it as visited when it is added to the queue (instead of line 62) to prevent it to be added
                # multiple times before being marked as visited.
                dq.append(x)


for i in range(n):
    if not visited[i]:
        visited[i] = True
        rep.append(i)
        BFS(i)
print(len(rep) - 1)
for i in range(1, len(rep)):
    print(rep[i - 1] + 1, rep[i] + 1)
