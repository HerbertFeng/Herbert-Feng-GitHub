'''
@Project : Class
@File : Minimum Spanning Trees (CSES).py
@Author : Herbert
@Date : 2/23/2025 3:54 PM
'''

'''
5 6
1 2 3
2 3 5
2 4 2
3 4 8
5 1 7
5 4 4
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
            return False
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        self.parent[p2] = p1
        self.rank[p1] += self.rank[p2]
        return True


import sys

input = sys.stdin.readline


def solve():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b, cost = map(int, input().split())
        roads.append((cost, a - 1, b - 1))
    roads.sort(key=lambda x: x[0])  # faster than roads.sort()
    cities = DSU(n)
    money, added = 0, 0
    for cost, a, b in roads:
        if cities.union(a, b):
            money += cost
            added += 1
    print('IMPOSSIBLE' if added != n - 1 else money)


solve()
