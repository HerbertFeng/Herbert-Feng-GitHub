'''
@Project : Class
@File : Template.py
@Author : Herbert
@Date : 1/29/2025 9:58 PM
'''
edge = [[1,2],[1,3],[2,3]]
n = len(edge)
rank = [0] * (n + 1)
parent = [i for i in range(n + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
        return False
    if rank[p1] > rank[p2]:
        parent[p2] = p1
        rank[p1] += rank[p2]
    else:
        parent[p1] = p2
        rank[p2] += rank[p1]
    return True