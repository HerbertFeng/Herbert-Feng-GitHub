'''
@Project : Class
@File : trains.py
@Author : Herbert
@Date : 2/16/2025 1:33 PM
'''


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        self.parent[p2] = p1
        self.rank[p1] += self.rank[p2]


def solve():
    n, e = map(int, input().split())
    vec = [DSU(n) for _ in range(e)]
    for _ in range(e):
        i, j, k = map(int, input().split())
        vec[k].union(i, j)
    c = int(input())
    for _ in range(c):
        u, v = map(int, input().split())
        ans = 0
        for i in range(e):
            if vec[i].find(u) == vec[i].find(v):
                ans += 1
        print(ans)


solve()

