'''
@Project : Class
@File : 111. Minimum Depth of Binary Tree.py
@Author : Herbert
@Date : 11/9/2023 9:11 PM
'''
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def build_tree(self, datas=[]):
        '''
        :param datas: [4,2,7,1,6,None,5]
        :return
        '''
        n = len(datas)
        if n == 0:
            return None

        def create_tree(idx):
            if idx >= n or datas[idx] is None:
                return None
            node = TreeNode(datas[idx])
            node.left = create_tree(2 * idx + 1)
            node.right = create_tree(2 * idx + 2)
            return node

        return create_tree(idx=0)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        depth = 1
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1


tree_obj = Solution()
tree = tree_obj.build_tree([3, 9, 20, None, None, 15, 7])
print(tree_obj.minDepth(tree))
