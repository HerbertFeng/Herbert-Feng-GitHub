'''
@Project : Class
@File : similar_pallindromes.py
@Author : Herbert
@Date : 11/03/2023 11:22
'''

# 15 min
# Please test if it works


def test(word):
    word_dict = {}
    for i in word:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1

    if len(word) % 2 == 1:
        odd = True
        for ele in word_dict.values():
            if ele % 2 == 1:
                if odd:
                    odd = False
                else:
                    return False
        return True
    else:
        for ele in word_dict.values():
            if ele % 2 == 1:
                return False
        return True


def main():
    new_word = str(input())
    change = {'p': 'q', 'b': 'd', 'a': 'e'}

    if test(word=new_word):
        print('Regular')
    else:
        lst = list(new_word)
        for i in range(len(lst)):
            if lst[i] in change:
                lst[i] = change[lst[i]]
        changed_word = ''.join(lst)
        if test(word=changed_word):
            print('Similar')
        else:
            print('Neither')


N = int(input())
for i in range(N):
    main()
