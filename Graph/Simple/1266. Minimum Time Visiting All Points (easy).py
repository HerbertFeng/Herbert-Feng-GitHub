'''
@Project : Class
@File : 1266. Minimum Time Visiting All Points (easy).py
@Author : Herbert
@Date : 12/3/2023 3:05 PM
'''


class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def travel(list1, list2):
            return max(abs(list1[0] - list2[0]), abs(list1[1] - list2[1]))

        ans = 0
        for i in range(1, len(points)):
            ans += travel(points[i - 1], points[i])
        return ans