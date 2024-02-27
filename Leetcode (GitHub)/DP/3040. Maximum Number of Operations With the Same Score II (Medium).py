'''
@Project : Class
@File : 3040. Maximum Number of Operations With the Same Score II (Medium).py
@Author : Herbert
@Date : 2/27/2024 11:09 AM
'''
from functools import cache
from typing import List


def maxOperations(nums: List[int]) -> int:
    first = nums[0] + nums[1]
    last = nums[-1] + nums[-2]
    both = nums[0] + nums[-1]

    @cache
    def dfs(i, j, val):
        if i >= j:
            return 0

        sA = dfs(i + 2, j, val) + 1 if val == nums[i] + nums[i + 1] else 0
        sB = dfs(i + 1, j - 1, val) + 1 if val == nums[i] + nums[j] else 0
        sC = dfs(i, j - 2, val) + 1 if val == nums[j] + nums[j - 1] else 0

        return max(sA, sB, sC)

    return max(dfs(2, len(nums) - 1, first), dfs(0, len(nums) - 3, last), dfs(1, len(nums) - 2, both)) + 1