#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：stoneye_private_study_note 
@File    ：0. Template.py
@Author  ：StoneYe
@Date    ：07/11/2023 10:39 
'''

'''
岛屿系列题目 => DFS 算法

那么如何在二维矩阵中使用 DFS 搜索呢？
如果你把二维矩阵中的每一个位置看做一个节点，
这个节点的上下左右四个位置就是相邻节点，
那么整个矩阵就可以抽象成一幅网状的「图」结构。
'''


from  typing import  List

# 二叉树遍历框架
def traverse(root):
    if not root:
        return
    traverse(root.left)
    traverse(root.right)


# 方向数组，分别代表上、下、左、右
dirs = [[-1,0], [1,0], [0,-1], [0,1]]

# 二维矩阵遍历框架
def dfs(grid: List[List[int]], i: int, j: int, visited: List[List[bool]]):
    m, n = len(grid), len(grid[0])
    if i < 0 or j < 0 or i >= m or j >= n:
        # 超出索引边界
        return
    if visited[i][j]:
        # 已遍历过 (i, j)
        return
    # 进入节点 (i, j)
    visited[i][j] = True
    # dfs(grid, i - 1, j, visited) # 上
    # dfs(grid, i + 1, j, visited) # 下
    # dfs(grid, i, j - 1, visited) # 左
    # dfs(grid, i, j + 1, visited) # 右
    for d in dirs:
        next_i,next_j = i + d[0],j + d[1]
        dfs(grid, next_i, next_j, visited)