'''
@Project : Class
@File : 1.Hungry_Cow.py
@Author : Herbert
@Date : 12/12/2023 11:35 AM
'''

'''
lines, days = map(int, input().split())


dic = {}
for _ in range(lines):
    k, v = map(int, input().split())
    if k <= days:
        dic[k] = v
        
count = 0
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

'''

N, T = map(int, input().split())
deliveries = [tuple(map(int, input().split())) for _ in range(N)] + [(T + 1, 0)]

remaining, total, last_d = 0, 0, 0
for d, b in deliveries:
    total += b
    remaining -= d - last_d
    last_d = d
    remaining = max(remaining, 0) + b

print(total - remaining)