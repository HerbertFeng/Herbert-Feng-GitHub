'''
@Project : Class
@File : 387. First Unique Character in a String (Easy).py
@Author : Herbert
@Date : 2/5/2024 11:44 AM
'''
from collections import defaultdict


class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = defaultdict(int)
        for i in s:
            dic[i] += 1

        for i in range(len(s)):
            if dic[s[i]] < 2:
                return i
        return -1
