'''
@Project : Class
@File : 169. Majority Element.py
@Author : Herbert
@Date : 11/11/2023 12:29 PM
'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele,count=0,0
        for num in nums:
            if count==0:
                ele=num
                count=1
            elif ele==num:
                count+=1
            else:
                count-=1
        return ele