'''
@Project : Class
@File : 2698. Find the Punishment Number of an Integer.py
@Author : Herbert
@Date : 2/15/2025 10:48 AM
'''

def punishmentNumber(n):
    """
    :type n: int
    :rtype: int
    """


    def part(num, target):
        if not num and target == 0:
            return True
        if target < 0:
            return False
        for i in range(len(num)):
            l = num[:i + 1]
            r = num[i + 1:]
            if part(r, target - int(l)):
                return True
        return False


    res = 0
    for i in range(1, n + 1):
        target = i * i
        if part(str(target), i):
            res += target
    return res