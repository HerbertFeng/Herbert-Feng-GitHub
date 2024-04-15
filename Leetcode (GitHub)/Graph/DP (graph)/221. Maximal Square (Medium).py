'''
@Project : Class
@File : 221. Maximal Square (Medium).py
@Author : Herbert
@Date : 4/15/2024 9:55 PM
'''


def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix or len(matrix) < 1:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])

    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    ans = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '1':
                dp[r + 1][c + 1] = min(dp[r][c], dp[r + 1][c], dp[r][c + 1]) + 1
                ans = max(ans, dp[r + 1][c + 1])
    return ans * ans
