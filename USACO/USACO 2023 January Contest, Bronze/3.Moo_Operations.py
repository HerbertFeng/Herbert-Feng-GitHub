'''
@Project : Class
@File : 3.Moo_Operations.py
@Author : Herbert
@Date : 12/14/2023 12:24 PM
'''


def check(word):
    ans = 0
    if word[0] != 'M':
        ans += 1
    if word[1] != 'O':
        ans += 1
    if word[2] != 'O':
        ans += 1
    return ans


