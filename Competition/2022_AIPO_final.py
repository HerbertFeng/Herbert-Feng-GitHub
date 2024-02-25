'''
@Project : Class
@File : 2022_AIPO_final.py
@Author : Herbert
@Date : 28/02/2023 19:48
'''


def isprime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def split_nums(num=0):
    ret = []
    for ele in str(num):
        ret.append(ele)
    return ret


def permutation(lst=[]):
    res = []
    path = []
    used_nums = [False] * len(lst)

    def back_tracking(lst):
        if len(path) == len(lst):
            res.append(path[:])
        for i in range(len(lst)):
            if used_nums[i]:
                continue
            path.append(lst[i])
            used_nums[i] = True
            back_tracking(lst)
            path.pop()
            used_nums[i] = False

    back_tracking(lst=lst)
    return res


def task1(n):
    count = 0
    nums = split_nums(num=n)
    p_lst = permutation(nums)

    for ele_lst in p_lst:
        ele_num = int(''.join(ele_lst))
        if isprime(n=ele_num):
            count += 1
    return count


def task2(n):
    nums = split_nums(num=n)
    p_lst = permutation(nums)
    for ele_lst in p_lst:
        ele_num = int(''.join(ele_lst))
        if not isprime(n=ele_num):
            return 0
    return 1


def main():
    a, n = map(int, input().split())
    if a == 0:
        print(task1(n=n))
    elif a == 1:
        print(task2(n=n))


main()
# print(permutation([1,2,3]))
