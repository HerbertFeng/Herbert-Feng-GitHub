'''
@Project : Class
@File : 1743. Restore the Array From Adjacent Pairs (Medium).py
@Author : Herbert
@Date : 12/2/2023 10:14 PM
'''
from collections import defaultdict


class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        pairs = defaultdict(list)

        for val in adjacentPairs:
            pairs[val[0]].append(val[1])
            pairs[val[1]].append(val[0])

        res = []
        start = 0

        for entry in pairs:
            if len(pairs[entry]) == 1:
                start = entry
                break

        left = -1000000
        res.append(start)

        for _ in range(len(adjacentPairs)):
            val = pairs[start]
            newval = val[0] if val[0] != left else val[1]
            res.append(newval)
            left = start
            start = newval

        return res
