'''
@Project : Class
@File : 1.Majority_Opinion.py
@Author : Herbert
@Date : 1/29/2024 4:29 PM
'''
'''def search(lst,ele):
    track = []
    for i in range(len(lst)):
        if lst[i] == ele:
            track.append(i)


    if len(track)==1:
        return False
    for i in range(len(track)-1):
        gap = 2
        for j in range(i+1, len(track)):
            if track[j] - track[i] - 1 < gap:
                return True
            else:
                gap += 1
    return False


def main():
    N = int(input())
    lst = list(map(int,input().split()))
    hays = sorted(set(lst))
    res = []
    for ele in hays:
        if search(lst,ele):
            res.append(ele)

    if len(res)==0:
        print(-1)
    else:
        print(' '.join(map(str,res)))

T = int(input())
for _ in range(T):
    main()
'''

def main():
    N = int(input())
    lst = list(map(int, input().split()))
    lst.append(float('inf'))

    res = []

    for i in range(len(lst)-2):
        if lst[i] == lst[i+1] or lst[i] == lst[i+2] :
            res.append(lst[i])


    if len(res) == 0:
        print(-1)
    else:
        print(' '.join(map(str, sorted(list(set(res))))))


T = int(input())
for _ in range(T):
    main()






