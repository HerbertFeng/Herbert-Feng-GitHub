'''
@Project : Class
@File : 695. Max Area of Island (Medium).py
@Author : Herbert
@Date : 2/5/2024 12:16 PM
'''


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, i, j))

        return ans

    def dfs(self, grid, i, j):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        grid[i][j] = 0

        return self.dfs(grid, i + 1, j) + self.dfs(grid, i - 1, j) + self.dfs(grid, i, j + 1) + self.dfs(grid, i,
                                                                                                         j - 1) + 1

