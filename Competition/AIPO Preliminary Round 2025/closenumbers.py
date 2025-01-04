'''
@Project : Class
@File : closenumbers.py
@Author : Herbert
@Date : 1/1/2025 6:33 PM
'''



def solve(n):
    i=0
    if n=='':
        return 0
    if n=='1':
        return 2
    res=0
    while i<len(n):
        if (i==0 and n[i]=='1') or n[i]=='0' or n[i]=='9':
            res+=1
        else:
            res+=2
        i+=1
    return res



n=input()
print(solve(n))

