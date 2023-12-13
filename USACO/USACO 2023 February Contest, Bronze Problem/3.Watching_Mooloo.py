'''
@Project : Class
@File : 3.Watching_Mooloo.py
@Author : Herbert
@Date : 12/12/2023 4:13 PM
'''


def check(a, b, k):
    if b - a > k + 1:
        return k + 1
    return b - a


def main():
    try:
        N, K = map(int, input().split())
        lst = list(map(int, input().split()))
        ans = K + 1
        for i in range(1, N):
            ans += check(a=lst[i - 1], b=lst[i], k=K)
        print(ans)
    except Exception as e:
        pass


main()
