'''
@Project : Class
@File : 3.Balancing_Bacteria.py
@Author : Herbert
@Date : 1/29/2024 6:29 PM
'''

def main():
    N = int(input())
    lst = list(map(int, input().split()))

    print(min(solution2(lst=lst.copy()),solution1(lst=lst.copy())))




def solution1(lst):
    res = 0
    target = -1
    for i in range(len(lst)):
        diff = target - lst[i]
        for j in range(i, len(lst)):
            lst[j] += diff * (j - i + 1)
        res += abs(diff)
        target -= 1

    return res + 1


def solution2(lst):
    res = 0
    target = 0
    for i in range(len(lst)):
        diff = target - lst[i]
        for j in range(i, len(lst)):
            lst[j] += diff * (j - i + 1)
        res += abs(diff)
        target += 1

    return res + 1


main()





