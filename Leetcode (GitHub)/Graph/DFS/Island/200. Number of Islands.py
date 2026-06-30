#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：stoneye_private_study_note 
@File    ：200. Number of Islands.py
@Author  ：StoneYe
@Date    ：07/11/2023 10:44 
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    count+=1
        return count

    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>= len(grid[0]) or grid[i][j]!='1':
            return
        grid[i][j] = '0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)

solution_obj = Solution()
print(solution_obj.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
