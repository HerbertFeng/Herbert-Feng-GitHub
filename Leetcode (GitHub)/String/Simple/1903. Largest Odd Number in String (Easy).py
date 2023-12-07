'''
@Project : Class
@File : 1903. Largest Odd Number in String (Easy).py
@Author : Herbert
@Date : 12/7/2023 11:10 PM
'''


class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ''
