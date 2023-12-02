'''
@Project : Class
@File : 153. Find Minimum in Rotated Sorted Array (medium).py
@Author : Herbert
@Date : 12/2/2023 9:16 PM
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
