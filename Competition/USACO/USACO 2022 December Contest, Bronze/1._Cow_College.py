'''
@Project : Class
@File : 1._Cow_College.py
@Author : Herbert
@Date : 12/14/2023 3:04 PM
'''
from collections import defaultdict


def main():
    N = int(input())
    cows = defaultdict(int)
    lst = list(map(int,input().split()))
    for i in range(N):
        cows[lst[i]]+=1

    new_cows = dict(sorted(cows.items(), key=lambda x: x[0], reverse=True))

    res = 0
    count = 0
    tuition = 0

    for price,amount in new_cows.items():
        count+=amount
        if price*count >= res:
            res = price*count
            tuition = price
    print(str(res)+' '+str(tuition))
main()