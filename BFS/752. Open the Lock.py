'''
@Project : Class
@File : 752. Open the Lock.py
@Author : Herbert
@Date : 11/9/2023 10:47 PM
'''
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def change(src: str):
            res = []
            for i, ch in enumerate(src):
                num = int(ch)
                res.append(src[:i] + str((num - 1) % 10) + src[i + 1:])
                res.append(src[:i] + str((num + 1) % 10) + src[i + 1:])
            return res

        depth, visited, q = -1, set(deadends), deque(['0000'])

        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                node = q.popleft()
                if node == target:
                    return depth
                if node in visited:
                    continue
                visited.add(node)
                q.extend(change(src=node))

        return -1

solution_obj = Solution()
print(solution_obj.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
