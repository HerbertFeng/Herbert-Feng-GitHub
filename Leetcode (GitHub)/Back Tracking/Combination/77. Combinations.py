'''
@Project : Class
@File : 77. Combinations.py
@Author : Herbert
@Date : 11/7/2023 8:18 PM
'''

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        path = []

        def backtracking(idx):
            if len(path) == k:
                res.append(path.copy())
                return
            for i in range(idx, n + 1):
                path.append(i)
                backtracking(i + 1)
                path.pop()

        backtracking(idx=1)
        return res


solution_obj = Solution()
print(solution_obj.combine(n=5, k=2))

