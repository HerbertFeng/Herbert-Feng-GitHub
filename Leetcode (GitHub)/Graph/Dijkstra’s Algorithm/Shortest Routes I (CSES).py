'''
@Project : Class
@File : Shortest Routes I (CSES).py
@Author : Herbert
@Date : 2/26/2025 11:19 PM
'''
import heapq
import sys

input = sys.stdin.readline

'''
3 4
1 2 6
1 3 2
3 2 3
1 3 4
'''

n,m  = map(int,input().split())
adj = [[] for _ in range(n)]
dist = [float('inf')]*n
for _ in range(m):
    a,b,c = map(int,input().split())
    adj[a-1].append((b-1,c))

hp = []
heapq.heappush(hp,(0,0))
dist[0] = 0

while hp:
    cost,dest = heapq.heappop(hp)
    if cost != dist[dest]:
        continue
    for d,c in adj[dest]:
        if dist[d]> cost+c:
            dist[d] = cost+c
            heapq.heappush(hp,(dist[d],d))

for i in range(n):
    print(dist[i], end = ' ')