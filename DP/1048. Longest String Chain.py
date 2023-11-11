'''
@Project : Class
@File : 1048. Longest String Chain.py
@Author : Herbert
@Date : 11/11/2023 12:53 PM
'''
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def helper(word1, word2):
            len1, len2 = len(word1), len(word2)
            if len1 + 1 != len2:
                return False
            i = 0
            for c in word2:
                if i == len1:
                    return True
                if word1[i] == c:
                    i += 1
            return i == len1

        words.sort(key=len)
        n = len(words)
        ans = 1
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            for j in range(i):
                if helper(words[j], words[i]) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                ans = max(dp[i], ans)
        return ans

