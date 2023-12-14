'''
@Project : Class
@File : 1.Leaders.py
@Author : Herbert
@Date : 12/13/2023 8:33 PM
'''

def main(N = 4, breed = 'GHHG', nums = '2 4 3 4'):
    N = int(N)
    breed = list(breed)
    nums = list(map(int,nums.split()))
    G = []
    H = []
    for i in range(N):
        if breed[i]=='H':
            H.append(breed[i:nums[i]])
        else:
            G.append(breed[i:nums[i]])

    print(G)
    print(H)
main()



