'''
@Project : Class
@File : Panda_Reserve.py
@Author : Herbert
@Date : 2/1/2024 11:52 AM
'''


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def main():
    # input all the given
    task = int(input())
    n, m, p = map(int, input().split())
    bear_x, bear_y, k, S = map(int, input().split())
    food = set()
    for _ in range(p):
        food_x, food_y = map(int, input().split())
        food.add((food_x, food_y))

    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    # change the panda's code
    code = decimalToBinary(k)[-S:]
    teddy_code = ''
    for i in range(len(code)):
        if code[i] == '0':
            teddy_code += '1'
        else:
            teddy_code += '0'

    teddy_code = teddy_code

    if task == 1:
        visited = set()

        def dfs(x, y):
            if x <= 0 or y <= 0 or x > n or y > m or teddy_code != decimalToBinary(graph[x - 1][y - 1])[-S:] or (
                    x, y) in visited:
                return 0
            visited.add((x, y))
            return dfs(x - 1, y) + dfs(x, y - 1) + dfs(x + 1, y) + dfs(x, y + 1) + 1

        print(dfs(bear_x, bear_y))

    if task == 2:

        queue = [(bear_x, bear_y)]
        visited = set()
        ans_time = 0
        time = 0
        num = 0
        while queue and ans_time == 0:
            size = len(queue)
            for _ in range(size):

                x, y = queue.pop(0)
                if x <= 0 or y <= 0 or x > n or y > m or teddy_code != decimalToBinary(graph[x - 1][y - 1])[-S:] or (
                        x, y) in visited:
                    continue
                if (x, y) in food:
                    ans_time = time
                    num += 1
                visited.add((x, y))

                queue.append((x - 1, y))
                queue.append((x + 1, y))
                queue.append((x, y - 1))
                queue.append((x, y + 1))

            time += 1

        print('{} {}'.format(str(ans_time), str(num)))


main()
