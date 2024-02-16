'''
@Project : Class
@File : 204. Count Primes (Medium).py
@Author : Herbert
@Date : 2/16/2024 2:30 PM
'''
import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        ans = 0
        for i in range(n):
            if is_prime[i]:
                ans += 1

        return ans