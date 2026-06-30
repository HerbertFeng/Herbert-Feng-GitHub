#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：stoneye_private_study_note 
@File    ：1020. Number of Enclaves.py
@Author  ：StoneYe
@Date    ：07/11/2023 12:04 
'''

'''
 除去四个边（淹没四边的陆地），剩下的有多少个1（陆地）即可。
'''

from typing import List


class Solution:

    def dfs_sesrch(self, grid, rows, cols, i, j, dirs):
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return
        if grid[i][j] == 0:
            return

        # 1->0 淹没陆地
        grid[i][j] = 0

        for (row, col) in dirs:
            next_i, next_j = i + row, j + col
            self.dfs_sesrch(grid, rows, cols, next_i, next_j, dirs)

    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = 0

        for i in range(rows):
            # left edge
            self.dfs_sesrch(grid, rows, cols, i, 0, dirs)
            # right edge
            self.dfs_sesrch(grid, rows, cols, i, cols - 1, dirs)
        for j in range(cols):
            # top edge
            self.dfs_sesrch(grid, rows, cols, 0, j, dirs)
            # bottom edge
            self.dfs_sesrch(grid, rows, cols, rows - 1, j, dirs)

        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i][j] == 1:
                    ans += 1

        return ans


solution_obj = Solution()
print(solution_obj.numEnclaves(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
