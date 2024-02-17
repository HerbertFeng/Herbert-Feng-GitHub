'''
@Project : Class
@File : Loan.py
@Author : Herbert
@Date : 2/17/2024 12:22 PM
'''

test = [2,2,2]
def main():
    laptop, task = map(int, input().split())
    net = 0
    negative = 0
    positive = 0
    ans = 0
    for i in range(task):
        k = int(input())
        net += k
        if net < 0:
            net -=k
            new = negative - k
            if negative == 0:
                ans += 1
                negative = new

            if new > laptop:
                negative = 0
                ans += 1

        if net > laptop:
            net -=k
            new_p = positive + k
            if positive == 0:
                ans += 1
                positive = new_p
            if new_p > laptop:
                positive = 0
                ans += 1

    print(ans)


main()
