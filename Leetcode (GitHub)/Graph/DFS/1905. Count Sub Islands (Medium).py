'''
@Project : Class
@File : 1905. Count Sub Islands (Medium).py
@Author : Herbert
@Date : 2/7/2024 11:41 PM
'''


def countSubIslands(grid1, grid2):
    """
    :type grid1: List[List[int]]
    :type grid2: List[List[int]]
    :rtype: int
    """

    def dfs(i, j):
        # come to the boundary of grid2
        if i < 0 or j < 0 or i >= len(grid2) or j >= len(grid2[0]) or grid2[i][j] == 0:
            return True
        # one of the cells is water and another is island --> cannot be a sub-island
        # elif (grid1[i][j] == 0 and grid2[i][j] == 1) or (grid1[i][j] == 1 and grid2[i][j] == 0):
        elif grid1[i][j] == 0:  # implicit grid2[i][j] == 1
            return False

        # both are 1s --> islands
        grid2[i][j] = 0

        l = dfs(i - 1, j)
        r = dfs(i + 1, j)
        t = dfs(i, j - 1)
        b = dfs(i, j + 1)

        # if all direction matches, an island is found
        return l and r and t and b

    totalN = 0
    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            if grid2[i][j] == 1:
                if dfs(i, j):
                    totalN += 1

    return totalN
