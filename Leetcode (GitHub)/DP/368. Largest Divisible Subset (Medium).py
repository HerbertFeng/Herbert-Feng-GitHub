'''
@Project : Class
@File : 368. Largest Divisible Subset (Medium).py
@Author : Herbert
@Date : 2/9/2024 11:44 AM
'''


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()

        dp = [[num] for num in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]

        return max(dp, key=len)