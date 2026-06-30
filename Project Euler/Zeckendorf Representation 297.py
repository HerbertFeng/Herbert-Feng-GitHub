'''
@Project : Class
@File : Zeckendorf Representation 297.py
@Author : Herbert
@Date : 30/06/2026 16:03
'''
import sys
from bisect import bisect_right

sys.setrecursionlimit(10**6)
lst = [1,2]
n = 10**17

while lst[-1]<n:
    lst.append(lst[-1]+lst[-2])

res = [1,2]
for i in range(2,len(lst)):
    v = res[-1]+res[-2]+lst[i-2]-1
    res.append(v)

#print(lst)
#print(res)

def main(k,level):
    if k==0:
        return 0
    j = bisect_right(lst, k) - 1
    v = lst[j]

    return main(k-v,level+1) + res[j] + lst[j]*level -1


def test(n):
    dp = [0]*n
    for i in range(1,n):
        j = bisect_right(lst, i) - 1
        dp[i] = dp[i-lst[j]]+1

    '''
    k = []
    for i in range(len(lst)):
        k.append(sum(dp[:lst[i]+1]))
    #print(k)
    '''

    print(sum(dp))

#test(n)
print(main(10**17,0))