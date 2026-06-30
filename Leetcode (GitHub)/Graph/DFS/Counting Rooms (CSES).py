'''
@Project : Class
@File : Counting Rooms (CSES).py
@Author : Herbert
@Date : 2/25/2025 11:10 AM
'''
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
'''
5 8
########
#..#...#
####.#.#
#..#...#
########
'''

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
d = [1, 0, -1, 0, 1]


def dfs(i, j):
    if 0 <= i < n and 0 <= j < m and grid[i][j] != '#' and not visited[i][j]:
        visited[i][j] = True
        for x in range(4):
            dfs(i + d[x], j + d[x + 1])
    return



res = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j] == '.':
            dfs(i, j)
            res += 1

print(res)

