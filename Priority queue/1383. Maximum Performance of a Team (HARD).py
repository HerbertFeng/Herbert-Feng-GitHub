'''
@Project : Class
@File : 1383. Maximum Performance of a Team (HARD).py
@Author : Herbert
@Date : 11/30/2023 8:37 PM
'''

import heapq
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        performances = sorted(zip(speed, efficiency), key=lambda x: x[1], reverse=True)
        ans = 0
        h = []
        total_speed = 0
        for s, e in performances:
            total_speed += s
            heapq.heappush(h, s)
            ans = max(ans, total_speed * e)
            if len(h) == k:
                total_speed -= heapq.heappop(h)
        return ans % (10 ** 9 + 7)

solution_obj = Solution()
print(solution_obj.maxPerformance(n = 3, speed = [2,8,2], efficiency = [2,7,1], k = 2))
