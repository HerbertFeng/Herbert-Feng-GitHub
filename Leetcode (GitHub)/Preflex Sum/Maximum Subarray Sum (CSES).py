'''
@Project : Class
@File : Maximum Subarray Sum (CSES).py
@Author : Herbert
@Date : 2/25/2025 1:51 PM
'''
'''
8
-1 3 -2 5 3 -5 2 2
10
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
'''

# max sub array i ~ j = max(psum[j]-psum[i-1]) = max(psum[j]) - min(psum[i-1]) for i<j
# optimised
n = int(input())
lst = list(map(int,input().split()))
cur = 0

mn = 0
res = lst[0]
for num in lst:
    cur += num
    res = max(res,cur-mn)
    mn = min(mn,cur)

print(res)

'''
n = int(input())
lst = list(map(int, input().split()))
cur = 0
psum = []
for i in range(n):
    cur += lst[i]
    psum.append(cur)

mn = 0
res = lst[0]
for num in psum:
    res = max(res, num - mn)
    mn = min(mn, num)

print(res)
'''