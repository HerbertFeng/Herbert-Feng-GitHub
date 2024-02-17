'''
@Project : Class
@File : Grid_Sums.py
@Author : Herbert
@Date : 1/9/2024 10:37 PM
'''


def main():
    n, m = map(int, input().split())
    for i in range(n):
        print(sum(list(map(int, input().split()))))


main()
