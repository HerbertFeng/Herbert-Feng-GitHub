'''
@Project : Class
@File : 5. Longest Palindromic Substring.py
@Author : Herbert
@Date : 11/8/2023 10:41 PM
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        maxlen = 1
        ans = s[0]

        for i in range(len(s)):
            odd = expand(i, i)
            if len(odd) > maxlen:
                maxlen = len(odd)
                ans = odd

        for i in range(len(s)):
            even = expand(i, i + 1)
            if len(even) > maxlen:
                maxlen = len(even)
                ans = even

        return ans
