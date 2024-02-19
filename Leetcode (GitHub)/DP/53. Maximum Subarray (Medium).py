'''
@Project : Class
@File : 53. Maximum Subarray (Medium).py
@Author : Herbert
@Date : 2/19/2024 12:10 PM
'''


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    best, sum = nums[0], nums[0]

    for i in range(1, len(nums)):
        sum = max(nums[i], sum + nums[i])
        best = max(sum, best)
    return best
