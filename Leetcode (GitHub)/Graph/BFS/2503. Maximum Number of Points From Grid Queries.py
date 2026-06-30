'''
@Project : Class
@File : 2503. Maximum Number of Points From Grid Queries.py
@Author : Herbert
@Date : 3/28/2025 8:37 PM
'''
import heapq


class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        rows,cols = len(grid),len(grid[0])
        Dir = [0,1,0,-1,0]

        queries = sorted([(val,idx) for idx,val in enumerate(queries)])
        res = [0]*len(queries)

        hp = [(grid[0][0],0,0)]
        vis = {(0, 0)}
        points = 0

        for val,idx in queries:
            while hp and hp[0][0]<val:
                _,r,c = heapq.heappop(hp)
                points+=1
                for i in range(4):
                    nr,nc = r+Dir[i],c+Dir[i+1]
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in vis:
                        vis.add((nr,nc))
                        heapq.heappush(hp,(grid[nr][nc],nr,nc))
            res[idx] = points
        return res

