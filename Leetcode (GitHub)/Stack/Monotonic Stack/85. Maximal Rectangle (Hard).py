'''
@Project : Class
@File : 85. Maximal Rectangle (Hard).py
@Author : Herbert
@Date : 4/14/2024 10:00 PM
'''


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        heights = [0] * len(matrix[0])
        ans = 0
        for row in matrix:
            for j, v in enumerate(row):
                if v == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.largestRectangleArea(heights))
        return ans

    def largestRectangleArea(self, height):
        """
        :type heights: List[int]
        :rtype: int
        """
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i]<height[stack[-1]]:
                h = height[stack.pop()]
                w = i-stack[-1]-1
                ans = max(ans,h*w)
            stack.append(i)
        height.pop()
        return ans