#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：stoneye_private_study_note 
@File    ：1905. Count Sub Islands.py
@Author  ：StoneYe
@Date    ：07/11/2023 15:57 
'''

from  typing import List

class Solution:

    def dfs_search(self,grid,rows,cols,i,j,dirs):
        if i<0 or j<0 or i>=rows or j>=cols:
            return []
        if grid[i][j] ==0:
            return  []
        grid[i][j] = 0

        ans = [(i,j)]
        for row,col in dirs:
            next_i,next_j = i + row, j + col
            ans.extend(self.dfs_search(grid,rows,cols,next_i,next_j,dirs))
        return ans

    def get_islands_list(self,grid):

        rows,cols = len(grid),len(grid[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        islands_list=[]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    continue
                islands_list.append(self.dfs_search(grid,rows,cols,i,j,dirs))
        return islands_list

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        islands_list1 = self.get_islands_list(grid=grid1)
        islands_list2 = self.get_islands_list(grid=grid2)

        ans =0
        for ele2 in islands_list2:
            for ele1 in islands_list1:
                if len(set(ele2) - set(ele1)) ==0:
                    ans+=1
        return ans


solution_obj = Solution()
print(solution_obj.countSubIslands(grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
                                   grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))

