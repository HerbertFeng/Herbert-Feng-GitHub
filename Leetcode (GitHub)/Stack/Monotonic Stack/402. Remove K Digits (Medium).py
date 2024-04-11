'''
@Project : Class
@File : 402. Remove K Digits (Medium).py
@Author : Herbert
@Date : 4/11/2024 10:20 PM
'''


def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    stk = []
    remain = len(num) - k
    for c in num:
        while k and stk and stk[-1] > c:
            stk.pop()
            k -= 1
        stk.append(c)
    return ''.join(stk[:remain]).lstrip('0') or '0'
