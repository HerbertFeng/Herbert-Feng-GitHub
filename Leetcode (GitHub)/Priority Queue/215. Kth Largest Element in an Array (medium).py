'''
@Project : Class
@File : 215. Kth Largest Element in an Array (medium).py
@Author : Herbert
@Date : 11/29/2023 11:43 PM
'''
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        for _ in range(k):
            topk = heapq.heappop(nums)

        return -topk
