'''
@Project : Class
@File : 1962. Remove Stones to Minimize the Total (medium).py
@Author : Herbert
@Date : 11/29/2023 11:38 PM
'''
import heapq

class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(piles)):
            piles[i] = -piles[i]

        heapq.heapify(piles)

        for i in range(k):
            largest = heapq.heappop(piles)
            largest = largest // 2
            heapq.heappush(piles, largest)

        return -sum(piles)