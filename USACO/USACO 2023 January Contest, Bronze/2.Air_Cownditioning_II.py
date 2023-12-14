'''
@Project : Class
@File : 2.Air_Cownditioning_II.py
@Author : Herbert
@Date : 12/14/2023 10:08 AM
'''


def combination(datas=[]):
    path = []
    result = []

    def back_tracking(datas, index):
        result.append(path[:])

        for i in range(index, len(datas)):
            path.append(datas[i])
            back_tracking(datas, index=i + 1)
            path.pop()

    back_tracking(datas=datas, index=0)

    return result


def iscool(lst=[]):
    for ele in lst:
        if ele > 0:
            return False
    return True


def main():
    res = float('inf')
    cows, air = map(int, input().split())
    stalls = [0] * (100)
    for _ in range(cows):
        a, b, cool = map(int, input().split())
        for j in range(a - 1, b):
            stalls[j] = max(stalls[j], cool)

    if air == 4:
        comb = combination(datas=[0, 1, 2, 3])
    else:
        comb = combination(datas=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    dic = {}
    for i in range(air):
        s, t, p, m = map(int, input().split())
        dic[i] = [s, t, p, m]

    for choose in comb:
        cost = 0
        stall = stalls.copy()
        for i in choose:

            for j in range(dic[i][0] - 1, dic[i][1]):
                stall[j] -= dic[i][2]
            cost += dic[i][3]

        if iscool(lst=stall):
            res = min(res, cost)

    print(res)


main()
