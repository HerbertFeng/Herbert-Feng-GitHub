'''
@Project : Class
@File : smooth_numbers.py
@Author : Herbert
@Date : 11/03/2023 11:46
'''


# 8 min
# Please test if it works

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def main():
    k, n = map(int, input().split())
    ans = 1
    for i in range(2, n + 1):
        if max(prime_factors(i)) <= k:
            ans += 1
    print(ans)


main()
