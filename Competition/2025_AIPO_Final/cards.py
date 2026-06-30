'''
@Project : Class
@File : cards.py
@Author : Herbert
@Date : 2/15/2025 1:22 PM
'''
import math



def GCD(a, b):
    if a<b:
        a,b = b,a
    if b == 0:
        return a
    else:
        return GCD(b, a % b)



def factors(n):

    factors_set = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            factors_set.add(i)
            factors_set.add(n // i)
    return factors_set




def test(i,lst,k,start):

    for j in range(start,k,2):
        if lst[j]%i==0:
            return 0
    return i

def check(odd,even,lst,k):
    if test(odd, lst, k, 0) != 0:
        return odd
    if test(even, lst, k, 1) != 0:
        return even
    return 'UNWINNABLE'



n = int(input())
for _ in range(n):
    k = int(input())
    lst = list(map(int,input().split()))
    if k==1:
        print(lst[0])
    else:
        even = lst[0]
        odd = lst[1]

        for i in range(k):
            if i%2==0:
                even = math.gcd(even,lst[i])
            else:
                odd = math.gcd(odd,lst[i])



        print(check(odd,even,lst,k))







