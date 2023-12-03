'''
@Project : Class
@File : 373. Find K Pairs with Smallest Sums (Medium).py
@Author : Herbert
@Date : 12/3/2023 10:32 PM
'''
import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or not k:
            return []

        visited = set((0, 0))
        hp = []
        output = []

        heapq.heappush(hp, (nums1[0] + nums2[0], 0, 0))

        while len(output) < k and hp:

            s, n1, n2 = heapq.heappop(hp)
            output.append([nums1[n1], nums2[n2]])

            if n1 + 1 < len(nums1) and (n1 + 1, n2) not in visited:
                heapq.heappush(hp, (nums1[n1 + 1] + nums2[n2], n1 + 1, n2))
                visited.add((n1 + 1, n2))
            if n2 + 1 < len(nums2) and (n1, n2 + 1) not in visited:
                heapq.heappush(hp, (nums1[n1] + nums2[n2 + 1], n1, n2 + 1))
                visited.add((n1, n2 + 1))

        return output