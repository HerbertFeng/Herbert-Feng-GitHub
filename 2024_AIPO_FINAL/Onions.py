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
