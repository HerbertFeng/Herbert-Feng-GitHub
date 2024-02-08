'''
@Project : Class
@File : 279. Perfect Squares (Medium).py
@Author : Herbert
@Date : 2/8/2024 1:13 PM
'''


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        count = 1
        while count * count <= n:
            sq = count * count
            for i in range(sq, n + 1):
                dp[i] = min(dp[i], dp[i - sq] + 1)
            count += 1
        return dp[n]
