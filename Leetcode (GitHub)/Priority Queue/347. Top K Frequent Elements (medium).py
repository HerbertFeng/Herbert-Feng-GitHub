'''
@Project : Class
@File : 347. Top K Frequent Elements (medium).py
@Author : Herbert
@Date : 11/30/2023 9:15 AM
'''
import heapq
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''
        dic = {}
        res=[]
        freq = [[] for _ in range(len(nums)+1)]

        for i in nums:
            dic[i] = 1+ dic.get(i,0)
        for n,c in dic.items():
            freq[c].append(n)

        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
        '''
        cnt_dct = Counter(nums)
        hp = []

        for key, value in cnt_dct.items():
            heapq.heappush(hp, (-value, key))

        return [heapq.heappop(hp)[1] for _ in range(k)]
