'''
@Project : Class
@File : 1254. Number of Closed Islands (Medium).py
@Author : Herbert
@Date : 2/5/2024 11:57 PM
'''


class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and self.dfs(grid, i, j):
                    ans += 1

        return ans

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
        if grid[i][j] == 1:
            return True
        grid[i][j] = 1
        left = self.dfs(grid, i, j - 1)
        right = self.dfs(grid, i, j + 1)
        up = self.dfs(grid, i - 1, j)
        down = self.dfs(grid, i + 1, j)
        return left and right and up and down