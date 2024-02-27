'''
@Project : Class
@File : 486. Predict the Winner (Medium).py
@Author : Herbert
@Date : 2/27/2024 10:30 AM
'''
from functools import cache
from typing import List


def predictTheWinner(nums: List[int]) -> bool:
    @cache
    def dfs(i, j):
        if i > j:
            return 0
        sA = nums[i] + min(dfs(i + 1, j - 1), dfs(i + 2, j))
        sB = nums[j] + min(dfs(i + 1, j - 1), dfs(i, j - 2))
        return max(sA, sB)

    total = sum(nums) / 2
    return True if dfs(0, len(nums) - 1) >= total else False
