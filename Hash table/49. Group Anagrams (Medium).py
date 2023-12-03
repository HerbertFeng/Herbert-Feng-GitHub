'''
@Project : Class
@File : 49. Group Anagrams (Medium).py
@Author : Herbert
@Date : 12/3/2023 8:46 PM
'''
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for word in strs:
            dic[tuple(sorted(word))].append(word)
        return list(dic.values())