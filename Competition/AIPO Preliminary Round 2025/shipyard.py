'''
@Project : Class
@File : shipyard.py
@Author : Herbert
@Date : 1/2/2025 10:33 AM
'''
n, m = map(int, input().split())


def solve(n, m):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i - j]) % 20242024
    return dp[-1] % 20242024


def solve1(n, m):
    if n==0 or m==0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    window_sum = 1

    for i in range(1, n + 1):
        dp[i] = window_sum % 20242024
        if i >= m:
            window_sum = (window_sum + dp[i] - dp[i - m]) % 20242024
        else:
            window_sum = (window_sum + dp[i]) % 20242024

    return dp[n] % 20242024


print(solve1(n, m))
