'''
@Project : Class
@File : The_Euclidean_Algorithm.py
@Author : Herbert
@Date : 1/11/2024 6:13 PM
'''


def Euclid(a, b):
    if a < b:
        a, b = b, a
    c = a % b
    if c == 0:
        return b
    return Euclid(b, c)


def main():
    x, y, z = map(int, input().split())
    print('YES' if Euclid(x, Euclid(y, z)) == 1 else 'NO')

main()
