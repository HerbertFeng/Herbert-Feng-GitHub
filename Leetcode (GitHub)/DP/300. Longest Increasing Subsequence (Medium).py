'''
@Project : Class
@File : 300. Longest Increasing Subsequence (Medium).py
@Author : Herbert
@Date : 2/19/2024 11:29 AM
'''


def lengthOfLIS(nums):
    n = len(nums)
    if n == 1:
        return 1
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
