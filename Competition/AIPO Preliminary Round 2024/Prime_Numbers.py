'''
@Project : Class
@File : Prime_Numbers.py
@Author : Herbert
@Date : 1/9/2024 10:46 PM
'''

def check(num):
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            return False
            break
    else:
        return True

def main():
    k = int(input())
    num=2
    while k:
        num+=1
        if check(num):
            k-=1

    print(num*num)
main()
