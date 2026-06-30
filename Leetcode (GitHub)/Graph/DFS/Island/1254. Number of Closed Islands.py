#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：stoneye_private_study_note 
@File    ：1254. Number of Closed Islands.py
@Author  ：StoneYe
@Date    ：07/11/2023 11:17 
'''

'''
那么如何判断「封闭岛屿」呢？其实很简单，把上一题中那些靠边的岛屿排除掉，剩下的不就是「封闭岛屿」了吗？

提前把靠边的陆地都淹掉，然后算出来的就是封闭岛屿了。

1) 先把四个边都遍历完(污染一遍)
2）回退成 number of Islands
'''

from typing import List


class Solution:

    def dfs_search(self, grid, rows, cols, i, j, visited, dirs):
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return
        if visited[i][j] or grid[i][j] == 1:
            return
        visited[i][j] = True
        for (row, col) in dirs:
            next_i, next_j = i + row, j + col
            self.dfs_search(grid, rows, cols, next_i, next_j, visited, dirs)

    def closedIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ans = 0

        for i in range(rows):
            # left edge
            self.dfs_search(grid, rows, cols, i, 0, visited, dirs)
            # right edge
            self.dfs_search(grid, rows, cols, i, cols - 1, visited, dirs)

        for j in range(cols):
            # top edge
            self.dfs_search(grid, rows, cols, 0, j, visited, dirs)
            # bottom edge
            self.dfs_search(grid, rows, cols, rows - 1, j, visited, dirs)

        # the rest islands are all closed islands.
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] or grid[i][j] == 1:
                    continue
                ans += 1
                self.dfs_search(grid, rows, cols, i, j, visited, dirs)

        return ans


solution_obj = Solution()
print(solution_obj.closedIsland(
    grid=[[1, 1, 1, 1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0, 1, 1, 0],
          [1, 0, 1, 0, 1, 1, 1, 0],
          [1, 0, 0, 0, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 0]]))
