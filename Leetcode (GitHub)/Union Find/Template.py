'''
@Project : Class
@File : Template.py
@Author : Herbert
@Date : 1/29/2025 9:58 PM
'''
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.size[p1] < self.size[p2]:
            p1, p2 = p2, p1
        self.parent[p2] = p1
        self.size[p1] += self.size[p2]
        return True