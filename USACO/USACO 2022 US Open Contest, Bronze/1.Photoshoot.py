'''
@Project : Class
@File : 1.Photoshoot.py
@Author : Herbert
@Date : 12/15/2023 1:05 PM
'''

def count(pos = ''):
    res = 0
    for i in range(2,len(pos),2):
        if pos[i]=='G':
            res+=1

def main():
    N = int(input())
    word = input()
    ans = 0
    for i in range(2,N,2):
        new_word = word[:i][::-1] + word[i:]
        ans = max(count(new_word,ans))
    print(ans)

main()



