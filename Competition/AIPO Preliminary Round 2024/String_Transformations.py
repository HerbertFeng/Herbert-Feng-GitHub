'''
@Project : Class
@File : String_Transformations.py
@Author : Herbert
@Date : 1/11/2024 7:42 PM
'''


def main():
    lines = list(map(str, input().split()))
    new_lines = lines[::-1]

    seen = set()
    vowel = {'a', 'e', 'i', 'o', 'u'}
    ans = []

    for i in range(len(new_lines)):
        if new_lines[i] in seen:
            continue
        seen.add(new_lines[i])

        if new_lines[i][0] not in vowel and len(new_lines[i]) % 2 == 1:
            ans.append(new_lines[i][::-1])
        else:
            ans.append(new_lines[i])
    print(' '.join(ans))


main()
