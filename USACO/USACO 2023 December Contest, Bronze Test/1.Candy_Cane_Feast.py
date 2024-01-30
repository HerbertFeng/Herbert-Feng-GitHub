'''
@Project : Class
@File : 1.Candy_Cane_Feast.py
@Author : Herbert
@Date : 12/16/2023 5:20 PM
'''
from collections import deque

N, M = map(int, input().split())

cows = list(map(int, input().split()))
candy = deque(map(int, input().split()))

for i in range(M):
    height = candy.popleft()
    base = 0
    for j in range(N):
        if cows[j] > base:

            if cows[j] < height:
                h = cows[j]
                cows[j] += cows[j] - base
                base = h

            else:
                cows[j] += height - base
                break

for i in range(N):
    print(cows[i])
