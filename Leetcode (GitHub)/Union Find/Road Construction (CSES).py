'''
@Project : Class
@File : Road Construction (CSES).py
@Author : Herbert
@Date : 2/23/2025 3:23 PM
'''


'''
5 3
1 2
1 3
4 5
'''

import sys

input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    parent = [i for i in range(n)]
    sz = [1] * n
    res = n
    compo = 1
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        nonlocal compo
        a, b = find(a), find(b)
        if a == b:
            return False
        if sz[a] < sz[b]:
            a, b = b, a
        parent[b] = a
        sz[a] += sz[b]
        compo = max(compo,sz[a])
        return True

    for _ in range(m):
        a,b = map(int,input().split())
        if union(a-1,b-1):
            res-=1
        print(res,compo)
solve()