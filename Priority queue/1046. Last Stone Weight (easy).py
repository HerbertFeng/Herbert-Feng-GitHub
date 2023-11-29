'''
@Project : Class
@File : 1046. Last Stone Weight (easy).py
@Author : Herbert
@Date : 11/29/2023 11:05 PM
'''
import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first - second != 0:
                heapq.heappush(stones, first - second)

        return 0 if len(stones) == 0 else -stones[0]
