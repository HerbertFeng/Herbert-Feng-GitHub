'''
@Project : Class
@File : Onions.py
@Author : Herbert
@Date : 2/17/2024 1:08 PM
'''
from collections import deque


def main():
    ans=0
    n = int(input())
    q = deque()
    q.append((0, 0))
    food = list(map(int, input().split()))
    for ele in food:
        size = len(q)
        if ele >= 0:
            for i in range(size):
                num,hp=q[i]
                q[i] = (num+1,hp+ele)
                ans = max(ans,num+1)

        else:
            for i in range(size):
                num, hp = q[i]
                if hp + ele >= 0:
                    q.append((num + 1, hp + ele))
                    ans = max(ans,num+1)



    print(ans)


main()

import time
from functools import cache
import random


def generate_data():
    lst = []
    for i in range(100):
        lst.append(random.randint(-1000, 1000))
    return lst


@cache
def f(cnt, h, i):
    if h < 0 or i == len(datas):
        return cnt

    return max(f(cnt + 1, h + datas[i], i + 1), f(cnt, h, i + 1))


def main():
    ans = 0
    # n = int(input())
    q = [(0, 0)]

    for ele in datas:
        size = len(q)
        if ele >= 0:
            for i in range(size):
                num, hp = q[i]
                q[i] = (num + 1, hp + ele)
                ans = max(ans, num + 1)

        else:
            for i in range(size):
                num, hp = q[i]
                if hp + ele >= 0:
                    q.append((num + 1, hp + ele))
                    ans = max(ans, num + 1)

    return ans


datas = generate_data()
print(datas)
start1 = time.time()
# print(f(0,0,0))
end1 = time.time()
print(main())
end2 = time.time()

print('function f, cost time {}\nfunction main, cost time{}'.format(end1 - start1, end2 - end1))

