'''
@Project : Class
@File : 647. Palindromic Substrings (Medium).py
@Author : Herbert
@Date : 2/10/2024 6:33 PM
'''


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def count(i, j, s):
            N = len(s)
            ans = 0
            while i >= 0 and j < N and s[i] == s[j]:
                i -= 1
                j += 1
                ans += 1
            return ans

        return sum(count(i, i, s) + count(i, i + 1, s) for i in range(len(s)))