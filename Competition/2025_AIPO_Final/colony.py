'''
@Project : Class
@File : colony.py
@Author : Herbert
@Date : 2/15/2025 1:01 PM
'''

def test(n,a,b):
    less = 0
    small = float('inf')
    for i in range(n):
        if a[i]-b[i]<0:
            if less==0:
                less = a[i]-b[i]
            else:
                return False
        else:
            small = min(small,a[i]-b[i])
    return True if small+less>=0 else False

n = int(input())
for i in range(n):
    k = int(input())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    if test(k,a,b):
        print('YES')
    else:
        print('NO')