#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：stoneye_private_study_note 
@File    ：200. Number of Islands.py
@Author  ：StoneYe
@Date    ：07/11/2023 10:44 
'''

from typing import List


class Solution:

    def dfs_search(self, grid, rows, cols, i, j, visited, dirs):

        #detect the edge
        if i < 0 or j < 0 or i >= rows or j >= cols:
            return
        if visited[i][j] or grid[i][j] == '0':
            return
        visited[i][j] = True
        #dfs search all dirs
        for (row, col) in dirs:
            next_i, next_j = i + row, j + col
            self.dfs_search(grid, rows, cols, next_i, next_j, visited, dirs)

    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * cols for _ in range(rows)]
        ans = 0

        for i in range(rows):
            for j in range(cols):
                if visited[i][j] or grid[i][j] == '0':
                    continue
                ans += 1
                self.dfs_search(grid, rows, cols, i, j, visited, dirs)

        return ans


solution_obj = Solution()
print(solution_obj.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
