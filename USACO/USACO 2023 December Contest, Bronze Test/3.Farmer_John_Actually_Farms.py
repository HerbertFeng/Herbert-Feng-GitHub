'''
@Project : Class
@File : 3.Farmer_John_Actually_Farms.py
@Author : Herbert
@Date : 12/16/2023 6:49 PM
'''

def check_equals(source, target):
    for s, t in zip(source, target):
        if s != t:
            return False
    return True


def check_is_infinity(heights=[], growths=[]):
    # heights=[4,4,4],growths=[8,8,6]  => True
    # heights=[4,5,4],growths=[8,8,6]  => False
    n = len(growths)
    growths_key_index_dict = {}
    for i in range(n):
        if growths[i] not in growths_key_index_dict:
            growths_key_index_dict[growths[i]] = []
        growths_key_index_dict[growths[i]].append(i)

    # detect the duplicate growth and init_height
    if len(growths_key_index_dict) != n:
        for k, v in growths_key_index_dict.items():
            if len(v) >= 1:
                if len(set([heights[idx] for idx in v])) != len(v):
                    return True
    return False


def sorted_index_single(datas=[]):
    n = len(datas)
    data_sorted = sorted(range(n), key=lambda i: datas[i])[::-1]
    return [data_sorted.index(i) for i in range(n)]


def sorted_index_pair(heights=[], growths=[]):
    # sorted pair first by growths, second by heights
    n = len(growths)
    data_pairs = list(zip(heights, growths))
    data_pairs_sorted = sorted(range(n), key=lambda i: (data_pairs[i][1], data_pairs[i][0]))[::-1]
    return [data_pairs_sorted.index(i) for i in range(n)]


def cal_min_days(heights=[], growths=[], target_index=[]):
    min_days = 0
    n = len(heights)
    while len(heights) != len(set(heights)) or not check_equals(source=sorted_index_single(heights),
                                                                target=target_index):
        for i in range(n):
            heights[i] += growths[i]
        min_days += 1
    return min_days


def solution(heights=[], growths=[], target_index=[]):
    if check_is_infinity(heights=heights, growths=growths):
        return -1
    predict_index = sorted_index_pair(heights=heights, growths=growths)
    if check_equals(predict_index, target_index):
        return cal_min_days(heights=heights, growths=growths, target_index=target_index)
    else:
        return -1


def main():
    samples = int(input())
    output_result = []
    for _ in range(samples):
        n = int(input())
        heights = list(map(int, input().split()))
        growths = list(map(int, input().split()))
        target_index = list(map(int, input().split()))
        result = solution(heights=heights, growths=growths, target_index=target_index)
        output_result.append(result)
    for out in output_result:
        print(out)


main()
