'''
@Project : Class
@File : 560. Subarray Sum Equals K (Medium).py
@Author : Herbert
@Date : 12/3/2023 11:30 PM
'''
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preflex_table = {0: 1}
        preflex_sum = 0
        ans = 0
        for num in nums:
            preflex_sum += num
            if preflex_sum - k in preflex_table:
                ans += preflex_table[preflex_sum - k]
            preflex_table[preflex_sum] = preflex_table.get(preflex_sum, 0) + 1

        return ans
