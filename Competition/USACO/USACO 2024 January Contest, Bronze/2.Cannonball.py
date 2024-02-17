'''
@Project : Class
@File : 2.Cannonball.py
@Author : Herbert
@Date : 1/29/2024 5:44 PM
'''
def main():
    N,S = map(int,input().split())
    dic = {}
    for i in range(1,N+1):
        a,b = map(int,input().split())
        dic[i]=[a,b]

    location = S
    val = 1
    target = 0
    move = 1
    while 0<location<N+1:
        if dic[location][0] == 1:
            if val>=dic[location][1]:
                target+=1
                dic[location][1] = float('inf')

        else:
            if move>0:
                move += dic[location][1]
            else:
                move -= dic[location][1]
            move*=-1
            val+=dic[location][1]

        location += move
    print(target)

main()


