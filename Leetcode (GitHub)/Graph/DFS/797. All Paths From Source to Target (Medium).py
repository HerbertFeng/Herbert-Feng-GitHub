'''
@Project : Class
@File : 797. All Paths From Source to Target (Medium).py
@Author : Herbert
@Date : 2/8/2024 12:12 PM
'''


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        d = {}
        for i in range(len(graph)):
            d[i] = graph[i]

        stack = [(0, [0])]
        res = []

        while stack:
            node, path = stack.pop()
            if node == len(graph) - 1:
                res.append(path)

            for nei in d[node]:
                stack.append((nei, path + [nei]))

        return res
