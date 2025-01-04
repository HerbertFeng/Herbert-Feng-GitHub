'''
@Project : Class
@File : earthquake.py
@Author : Herbert
@Date : 1/2/2025 1:41 AM
'''
n=int(input())
earth = list(input().split())

res = 0
i=0
while i<n:
    if earth[i] == '1' and i>1 and earth[i-1]=='0' and earth[i-2]=='0':
        k=0
        while i<n and earth[i]=='1':
            k+=1
            i+=1
        if i<n-1 and earth[i+1]=='0' and earth[i]=='0':
            res = max(res,k)
    else:
        i+=1

print(res)

