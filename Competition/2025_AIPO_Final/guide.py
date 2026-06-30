'''
@Project : Class
@File : guide.py
@Author : Herbert
@Date : 2/15/2025 11:42 AM
'''

#2025-01-01-01-2025-02-2026

a = input()
old_date = list(input().split('-'))
date = []
for i in range(len(old_date)):
    if len(old_date[i])>1:
        date.append(int(old_date[i]))
    else:
        date.append(0)

n = len(date)
def toint (s):
    if len(s)==1:
        return '0'+s
    return s

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(n-1,-1,-1):
    if i>=2 and len(old_date[i])>=4 and int(old_date[i][-4:])==2025  and len(old_date[i-1])==2 and len(old_date[i-2])>=2 and 12>=date[i-1]>=2:
        if date[i-1]==2 and 16<=int(old_date[i-2][-2:])<=28:
            print(old_date[i - 2][-2:] + '-' + old_date[i - 1] + '-' + old_date[i][-4:])
            break
        elif month[date[i-1]]>=int(old_date[i-2][-2:])>0:
            print(old_date[i - 2][-2:] + '-' + old_date[i - 1] + '-' + old_date[i][-4:])
            break
    elif i>=2 and len(old_date[i])>=4 and 2025<int(old_date[i][-4:])<2028 and len(old_date[i-1])==2 and len(old_date[i-1])==2 and len(old_date[i-2])>=2 and 0<=date[i-1]<=12 and month[date[i-1]]>=int(old_date[i-2][-2:])>0:
        print(old_date[i - 2][-2:] + '-' + old_date[i - 1] + '-' + old_date[i][-4:])
        break


