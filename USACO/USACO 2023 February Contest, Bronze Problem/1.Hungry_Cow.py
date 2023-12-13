'''
@Project : Class
@File : 1.Hungry_Cow.py
@Author : Herbert
@Date : 12/12/2023 11:35 AM
'''

lines, days = map(int, input().split())

count = 0
dic = {}
for _ in range(lines):
    k, v = map(int, input().split())
    if k <= days:
        dic[k] = v
stock = 0
ans = 0
while count <= days:
    if count in dic:
        stock += dic[count]
    if stock > 0:
        stock -= 1
        ans += 1
    count += 1
print(ans)
