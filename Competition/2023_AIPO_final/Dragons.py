'''
@Project : Class
@File : Dragons.py
@Author : Herbert
@Date : 2/3/2024 11:25 AM
'''


# I did the task 1 using bfs (queue). please check!
# for task 2, I think we should use dijkstra algorithm,
# but I need to also need to consider if the dragon can fly to the nex island.

def main():
    task = int(input())
    islands, routes = map(int, input().split())
    dragons = list(map(int, input().split()))
    island_map = {}
    for i in range(routes):
        a, b, d = map(int, input().split())
        if a in island_map:
            island_map[a][0].append(b)
            island_map[a][1].append(d)
        else:
            island_map[a] = [[b], [d]]

    if task == 1:
        res = dragons[0]
        queue = [1]
        seen = set()
        while queue:
            cur = queue.pop(0)

            for i in range(len(island_map[cur][0])):
                if island_map[cur][0][i] not in seen and island_map[cur][1][i] <= dragons[0]:
                    res = max(res, dragons[island_map[cur][0][i] - 1])
                    if island_map[cur][0][i] in island_map:
                        queue.append(island_map[cur][0][i])
                        seen.add(island_map[cur][0][i])

        print(res)

    if task == 2:
        pass


main()
