#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：stoneye_private_study_note 
@File    ：695. Max Area of Island.py
@Author  ：StoneYe
@Date    ：07/11/2023 12:31 
'''

'''
    设计dfs 函数：
        添加返回值，记录每次淹没的陆地的个数
'''

from typing import List


class Solution:

    def dfs_search(self, grid, rows, cols, i, j, dirs):
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return 0
        if grid[i][j] == 0:
            return 0

        grid[i][j] = 0
        areas = 0
        for row, col in dirs:
            next_i, next_j = i + row, j + col
            areas += self.dfs_search(grid, rows, cols, next_i, next_j, dirs)
        return 1 + areas

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        max_areas = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                max_areas = max(max_areas, self.dfs_search(grid, rows, cols, i, j, dirs))
        return max_areas


solution_obj = Solution()
print(solution_obj.maxAreaOfIsland(
    grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
