'''
@Project : Class
@File : 543. Diameter of Binary Tree (Easy).py
@Author : Herbert
@Date : 2/27/2024 10:05 AM
'''
from idlelib.tree import TreeNode


def diameterOfBinaryTree(self, root: TreeNode) -> int:
    def height(root):
        nonlocal diameter
        if not root:
            return 0

        left = height(root.left)
        right = height(root.right)
        diameter = max(diameter, left + right)
        return max(left, right) + 1

    diameter = 0
    height(root)
    return diameter
