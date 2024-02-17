'''
@Project : Class
@File : GCD.py
@Author : Herbert
@Date : 2/17/2024 11:02 AM
'''
def combine(n, k):
    res = []
    path = []

    def backtracking(idx):
        if len(path) == k:
            res.append(path.copy())
            return
        for i in range(idx, n):
            path.append(i)
            backtracking(i + 1)
            path.pop()

    backtracking(idx=0)
    return res

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


def main():
    task = int(input())
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    if task == 1:
        ans = gcd(lst[0], lst[1])
        for i in range(2, n):
            ans = gcd(ans, lst[i])
        print(ans)
    if task == 2:
        res = 0
        for i in range(n):
            ans = 0
            for j in range(n):
                if j != i:
                    ans = gcd(ans, lst[j])
            res = max(res, ans)
        print(res)
    if task == 3:
        res = 0
        comb = combine(n,2)
        for ele in comb:
            ans = 0

            for i in range(n):
                if i in ele:
                    continue
                ans = gcd(ans,lst[i])
            res = max(res,ans)
        print(res)




main()
