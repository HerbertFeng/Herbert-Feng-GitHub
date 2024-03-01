'''
@Project : Class
@File : 518. Coin Change II (Medium).py
@Author : Herbert
@Date : 3/1/2024 8:50 PM
'''


def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """

    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]