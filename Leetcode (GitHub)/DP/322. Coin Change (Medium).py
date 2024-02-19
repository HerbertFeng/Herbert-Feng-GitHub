'''
@Project : Class
@File : 322. Coin Change (Medium).py
@Author : Herbert
@Date : 2/19/2024 11:45 AM
'''


def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
