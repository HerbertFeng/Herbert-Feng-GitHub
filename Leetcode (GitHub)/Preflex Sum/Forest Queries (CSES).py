'''
@Project : Class
@File : Forest Queries (CSES).py
@Author : Herbert
@Date : 2/25/2025 9:33 PM
'''
import sys

input = sys.stdin.readline

'''
4 3
.*..
*.**
**..
****
2 2 3 4
3 1 3 1
1 1 2 2
'''


def solve():
    n, m = map(int, input().split())
    tree = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        for j, c in enumerate(input().strip()):
            is_tree = c == '*'
            tree[i + 1][j + 1] += tree[i][j + 1] + tree[i + 1][j] - tree[i][j] + is_tree
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(tree[x2][y2] - tree[x2][y1 - 1] - tree[x1 - 1][y2] + tree[x1 - 1][y1 - 1])

solve()
