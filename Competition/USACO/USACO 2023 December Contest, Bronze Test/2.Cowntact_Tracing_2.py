'''
@Project : Class
@File : 2.Cowntact_Tracing_2.py
@Author : Herbert
@Date : 12/16/2023 6:03 PM
'''

'''def spread(lst=[]):
    k = len(lst)
    for i in range(k):
        if lst[i] == 1:
            if 0 < i < k - 1:
                lst[i - 1] = -1
                lst[i + 1] = -1
    for i in range(k):
        if lst[i] == -1:
            lst[i] = 1
    return lst'''

'''
def count(lst=[], N=0):
    res = []
    for i in range(N):
        if lst[i] == 1:
            k = i
            while k < N and lst[k] == 1:
                lst[k] = 0
                k += 1

            if i == 0 or k == N:
                res.append((k - i - 1) * 2 + 1)

            else:
                res.append(k - i)

    return res


def calculate_min(count_cows=[]):
    smallest = min(count_cows)

    days = 0
    while smallest != 1 and smallest != 2:
        days += 1
        smallest -= 2
    total = sum(count_cows)
    return total - 2 * days * len(count_cows)


# print(count([1,1,1,1,1,1,0],7))

def main():
    length = int(input())
    cows = str(input())
    cows_lst = []
    for i in range(length):
        cows_lst.append(int(cows[i]))

    start = cows_lst.copy()
    start.insert(0, 0)

    end = cows_lst.copy()
    end.append(0)

    start_and_end = cows_lst.copy()
    start_and_end.insert(0, 0)
    start_and_end.append(0)

    count_cows = count(lst=cows_lst, N=length)
    print(count_cows)
    count_cows_with_start = count(lst=start, N=length + 1)
    print(count_cows_with_start)
    count_cows_with_end = count(lst=end, N=length + 1)
    print(count_cows_with_end)
    count_cows_with_start_and_end = count(lst=start_and_end, N=length + 2)
    print(count_cows_with_start_and_end)

    print(min(calculate_min(count_cows), calculate_min(count_cows_with_start), calculate_min(count_cows_with_end),
              calculate_min(count_cows_with_start_and_end)))


main()
'''

def calculate_min(count_cows=[]):
    smallest = min(count_cows)

    days = 0
    while smallest != 1 and smallest != 2:
        days += 1
        smallest -= 2
    total = sum(count_cows)
    return total - 2 * days * len(count_cows)

def calculate_min_with_start(count_cows=[]):
    smallest = min(count_cows)

    days = 0
    while smallest != 1 and smallest != 2:
        days += 1
        smallest -= 2
    first_day = (count_cows[0]-1)/2 +1
    first_day-=days
    other = count_cows[1:]
    total = sum(other)
    return total - 2 * days * len(other) + first_day

def calculate_min_with_end(count_cows=[]):
    smallest = min(count_cows)

    days = 0
    while smallest != 1 and smallest != 2:
        days += 1
        smallest -= 2
    last_day = (count_cows[-1]-1)/2 +1
    last_day-=days
    other = count_cows[:-1]
    total = sum(other)
    return total - 2 * days * len(other) + last_day

def calculate_min_with_start_and_end(count_cows=[]):
    smallest = min(count_cows)

    days = 0
    while smallest != 1 and smallest != 2:
        days += 1
        smallest -= 2
    first_day = (count_cows[0] - 1) / 2 + 1
    last_day = (count_cows[-1]-1)/2 +1
    first_day-=days
    last_day-=days
    other = count_cows[1:-1]
    total = sum(other)
    return total - 2 * days * len(other) + last_day + first_day


def main():
    length = int(input())
    cows = str(input()).split('0')

    cows_lst = []
    for i in range(len(cows)):
        if len(cows[i]) > 0:
            cows_lst.append(len(cows[i]))

    first = False
    end = False
    both = False
    if len(cows[0]) > 0:
        first = True
        lst_start=cows_lst.copy()
        lst_start[0] = (cows_lst[0] - 1) * 2 + 1
    if len(cows[-1]) > 0:
        end = True
        lst_end = cows_lst.copy()
        lst_end[-1] = (cows_lst[-1] - 1) * 2 + 1

    if len(cows[-1]) > 0 and len(cows[0]) > 0:
        both = True
        lst_start_and_end = cows_lst.copy()
        lst_start_and_end[0] = (cows_lst[0] - 1) * 2 + 1
        lst_start_and_end[-1] = (cows_lst[-1] - 1) * 2 + 1


    res = calculate_min(cows_lst)
    if first:
        res = min(calculate_min_with_start(lst_start),res)
    if end:
        res = min(calculate_min_with_end(lst_end,),res)
    if both:
        res = min(calculate_min_with_start_and_end(lst_start_and_end),res)

    print(int(res))

main()

'''1111110
1011100
1111111'''
