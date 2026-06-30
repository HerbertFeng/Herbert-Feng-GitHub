'''
@Project : Class
@File : palindrome.py
@Author : Herbert
@Date : 2/15/2025 11:16 AM
'''


def test(s):

    for i in range(len(s) + 1):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            new_s = s[:i] + c + s[i:]
            if new_s == new_s[::-1]:
                return new_s

    return "NONE"

n = int(input())
for _ in range(n):
    s = input()
    print(test(s))

