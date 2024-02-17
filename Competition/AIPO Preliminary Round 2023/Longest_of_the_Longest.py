'''
@Project : Class
@File : Longest_of_the_Longest.py
@Author : Herbert Feng
@Date : 17/02/2023 08:31
'''
import ast
import re
import string


def len_without_punctuation(text):
    count = 0
    for c in text:
        if c not in string.punctuation:
            count += 1
    return count

def longest_string(n):
    lst = ast.literal_eval(n)
    max_str=''
    max_str_num=0
    for i in lst:
        l=len_without_punctuation(i)
        if l>max_str_num:
            max_str=i
            max_str_num=l

    return max_str

def longest_word(n):
    word_lst=n.split()
    max_str = ''
    max_str_num = 0
    reverse=False
    for i in word_lst:
        l = len_without_punctuation(i)
        if l > max_str_num:
            max_str = i
            max_str_num = l
            reverse=False
        elif i==max_str:
            reverse=True
    stripe_str= max_str.strip(string.punctuation)
    if reverse:
        return stripe_str[::-1]
    else:
        return stripe_str

def longest_word_v1(n):
    res = re.findall( r'\w+|[^\s\w]+', n)
    max_str = ''
    max_str_num = 0
    reverse = False
    for i in res:
        l = len_without_punctuation(i)
        if l > max_str_num:
            max_str = i
            max_str_num = l
            reverse = False
        elif i == max_str:
            reverse = True

    if reverse:
        return max_str[::-1]
    else:
        return max_str


input_word = input()
longest = longest_string(input_word)
print(longest)
print(longest_word_v1(longest))










