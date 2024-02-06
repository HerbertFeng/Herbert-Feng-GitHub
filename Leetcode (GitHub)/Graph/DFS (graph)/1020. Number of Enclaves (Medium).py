'''
@Project : Class
@File : 1020. Number of Enclaves (Medium).py
@Author : Herbert
@Date : 2/6/2024 12:39 AM
'''


class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    flag, count = self.dfs(grid, i, j)
                    if flag:
                        ans += count

        return ans

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False, 0
        if grid[i][j] == 0:
            return True, 0

        grid[i][j] = 0
        left = self.dfs(grid, i, j - 1)
        right = self.dfs(grid, i, j + 1)
        up = self.dfs(grid, i - 1, j)
        down = self.dfs(grid, i + 1, j)
        return left[0] and right[0] and up[0] and down[0], left[1] + right[1] + up[1] + down[1] + 1
