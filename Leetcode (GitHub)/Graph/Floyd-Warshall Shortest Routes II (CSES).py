'''
@Project : Class
@File : Floyd-Warshall Shortest Routes II (CSES).py
@Author : Herbert
@Date : 2/26/2025 11:40 PM
'''

import sys

input = sys.stdin.readline
'''
4 3 5
1 2 5
1 3 9
2 3 3
1 2
2 1
1 3
1 4
3 2
'''
large = 10**9
n,m,q = map(int,input().split())
adj = [[float(large)]*n for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    if c<adj[a-1][b-1]:
        adj[a-1][b-1] = c
        adj[b-1][a-1] = c

for k in range(n):
    for i in range(n):
        for j in range(i+1,n):
            adj[i][j] = min(adj[i][j],adj[i][k]+adj[k][j])
            adj[j][i] = adj[i][j]

for _ in range(q):
    x,y = map(int,input().split())
    x,y=  x-1,y-1
    if x==y:
        print(0)
    elif adj[x][y]==large:
        print(-1)
    else:
        print(adj[x][y])