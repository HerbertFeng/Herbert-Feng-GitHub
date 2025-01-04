'''
@Project : Class
@File : division.py
@Author : Herbert
@Date : 1/2/2025 11:26 AM
'''
from collections import defaultdict

def solve(n,k,lst):
    s=defaultdict(int)
    for i in lst:
        s[i%k]+=1
    for i in range(n):
        if s[lst[i]%k]== 1:
            return i+1
    return -1

#print(solve(5,3,[1,31,15,36,55])) #-1

time=int(input())
for _ in range(time):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    print(solve(n,k,lst))

'''
7
3 2
1 2 3
2 2
15 16
4 2
1 2 4 5
2 2
15 15
5 3
10 7 4 5 3
5 3
1 31 15 36 55
1 3
5
'''