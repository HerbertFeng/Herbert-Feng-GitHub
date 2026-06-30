'''
@Project : Class
@File : 3108. Minimum Cost Walk in Weighted Graph.py
@Author : Herbert
@Date : 3/20/2025 10:50 AM
'''


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.weight = [-1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, weights):
        p1, p2 = self.find(x), self.find(y)
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        self.parent[p2] = p1
        self.rank[p1] += self.rank[p2]
        self.weight[p1] = self.weight[p2] = self.weight[p1] & self.weight[p2] & weights

    def min_cost(self, x, y):
        if x == y:
            return 0
        if self.find(x) != self.find(y):
            return -1
        return self.weight[self.find(x)]


class Solution(object):
    def minimumCost(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """
        uf = DSU(n)
        for x, y, z in edges:
            uf.union(x, y, z)
        return [uf.min_cost(x, y) for x, y in query]


s = Solution()
print(s.minimumCost(n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]))