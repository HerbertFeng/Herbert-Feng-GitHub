'''
@Project : Class
@File : Journey.py
@Author : Herbert
@Date : 2/17/2024 1:58 PM
'''


def main():
    paragraph, lines = map(int, input().split())
    for _ in range(paragraph):
        words = list(map(str, input().split()))

        space = 0
        total = 0
        i, j = 0, 0
        while i < len(words):
            if space + len(words[i]) + total < lines:
                total += len(words[i])
                if i != 0:
                    space += 1
                i += 1
            else:
                need_space = lines - total
                space1 = (need_space % (i - j)) * ' '
                space2 = (need_space // (i - j)) * ' '
                ans = words[j]
                for k in range(j+1, i):
                    if k == j + 1:
                        ans += space1 + space2 + words[k]
                    else:
                        ans += space2 + words[k]
                print(ans)
                total = 0
                space = 0
                j=i

        ans = words[j]
        for k in range(j + 1, len(words)):
            ans += ' ' + words[k]

        print(ans)
main()

