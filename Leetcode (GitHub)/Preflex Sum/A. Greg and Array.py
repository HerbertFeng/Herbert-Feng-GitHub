'''
@Project : Class
@File : A. Greg and Array.py
@Author : Herbert
@Date : 2/25/2025 10:58 PM
'''

import sys

input = sys.stdin.readline

# difference array: if you have multiple queries to increase an interval [l,r] by k,
# update s[l]+=k and s[r+1]-=k for each queries O(n).
# when you want the final result, run prefix sum on s.
# note that the increase at the start cancels out the decrease after the interval

'''
3 3 3
1 2 3
1 2 1
1 3 2
2 3 4
1 2
1 3
2 3
'''
#  double difference array
# https://codeforces.com/contest/295/problem/A
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
updates = []
for _ in range(m):
    updates.append(list(map(int, input().split())))

s = [0] * (m + 2)
add = [0] * (n + 2)

for _ in range(k):
    x, y = map(int, input().split())
    s[x] += 1
    s[y + 1] -= 1

for i in range(1, m + 1):
    s[i] += s[i - 1]
    add[updates[i - 1][0]] += s[i] * updates[i - 1][2]
    add[updates[i - 1][1] + 1] -= s[i] * updates[i - 1][2]

for i in range(1, n + 1):
    add[i] += add[i - 1]
    print(add[i] + arr[i - 1], end=' ')
