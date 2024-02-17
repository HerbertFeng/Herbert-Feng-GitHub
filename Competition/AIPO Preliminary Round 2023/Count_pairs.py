'''
@Project : Class
@File : Count_pairs.py
@Author : Herbert
@Date : 16/02/2023 11:13
'''
import math


def sieve(MAXN):
    spf = [0 for _ in range(MAXN)]
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2
    for i in range(3, math.ceil(math.sqrt(MAXN))):
        if (spf[i] == i):
            for j in range(i * i, MAXN, i):
                if (spf[j] == j):
                    spf[j] = i

    return spf

def get_prime_factor(n,lst):
    ans = []
    while n!=1:


        ans.append(lst[n])
        n = n // lst[n]


    return ans

def phi(n,lst):
    num=n
    if n==1:
        return 1

    for prime in set(get_prime_factor(n,lst)):

        num=num-num/prime
    return int(num)

def main(n,c):
    n=n//c
    lst = sieve(n + 1)
    dp=[0]*(n+1)
    dp[1]=1

    for i in range(2,n+1):
        dp[i]=dp[i-1]+phi(n=i,lst=lst)

    return dp[n]%1000000007

c,n=map(int,input().split())
print(main(n=n,c=c))





