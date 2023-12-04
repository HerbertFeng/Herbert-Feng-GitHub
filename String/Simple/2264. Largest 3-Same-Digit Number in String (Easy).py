'''
@Project : Class
@File : 2264. Largest 3-Same-Digit Number in String (Easy).py
@Author : Herbert
@Date : 12/4/2023 9:30 AM
'''


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            if str(i) * 3 in num:
                return str(i) * 3
        return ''
