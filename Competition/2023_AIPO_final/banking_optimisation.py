'''
@Project : Class
@File : banking_optimisation.py
@Author : Herbert
@Date : 11/03/2023 11:03
'''

import math, random

# which case do I need to return -1?
# Both of them didn't work when I submitted into the competition

# num, time = map(int, input().split())
num, time = -1, -1
lst = []


def bank1(time, lst):
    total = sum(lst)
    return int(math.ceil(total/time))



# def bank2(time, lst=i[]):
# #     total = sum(lst)
# #     if total < time:
# #         return 1
# #     if time == 1:
# #         return total
# #     for i in range(1, total):
# #         if total / i <= time:
# #             return

def bank2(time, lst):
    total = sum(lst)

    low = 0
    high = total + 10

    while (low < high):
        mid = (low + high) // 2

        if (total > time * mid):
            low = mid + 1
        else:
            high = mid


    if (total <= time * low):
        return low
    else:
        return -1


for _ in range(1):
    num = random.randint(1000, 100000)
    time = random.randint(1, 1000000)
    lst = [random.randint(1, 100000) for _ in range(num)]

    res1 = bank1(time, lst)
    res2 = bank2(time, lst)
    # assert(res1 == res2)

    if (res1 != res2):
        print(num, time, lst)
        print(res1)
        print(res2)
        break
