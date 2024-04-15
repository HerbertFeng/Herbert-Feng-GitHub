'''
@Project : Class
@File : 84. Largest Rectangle in Histogram (Hard).py
@Author : Herbert
@Date : 4/15/2024 1:06 AM
'''


def largestRectangleArea(height):
    """
    :type heights: List[int]
    :rtype: int
    """
    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans