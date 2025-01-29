'''
@Project : Class
@File : wells.py
@Author : Herbert
@Date : 1/3/2025 7:23 PM
'''
import heapq



def well_racing(test_cases):
    results = []

    for H, J, walls in test_cases:
        q=[(0, 0, 0)]
        heapq.heapify(q)  # (height, left or right, time)
        visited = {(0, 0)}  # (height, wall)
        wendy_wins = False
        wally_wins = False

        while q:
            height, wall, time = heapq.heappop(q)
            height = -height
            wally_height = time - 1

            if height <= wally_height:
                wally_wins = True

            if height >= H:
                wendy_wins = True
                break

            # Wendy's possible moves
            for new_height, new_wall in [
                (height + 1, wall),
                (height - 1, wall),
                (height + J, 1 - wall)
            ]:
                # Check if the move is valid
                if 0 <= new_height and (new_height, new_wall) not in visited:
                    if new_height >= H or walls[new_height][new_wall] == '.':
                        visited.add((new_height, new_wall))
                        heapq.heappush(q,(-new_height, new_wall, time + 1))

        if wally_wins and wendy_wins:
            results.append("WALLY")
        elif wendy_wins:
            results.append("WENDY")
        else:
            results.append("FORFEIT")

    return results


def main():
    T = int(input())
    test_cases = []
    for _ in range(T):
        H, J = map(int, input().split())
        walls = []
        for _ in range(H):
            s = input()
            walls.append([s[0], s[1]])
        walls = walls[::-1]
        test_cases.append((H, J, walls))

    results = well_racing(test_cases)
    print("\n".join(results))


main()

'''
2
7 3
#.
.#
.#
#.
..
.#
..
6 2
..
##
.#
#.
..
.#
'''
# output WENDY WALLY
'''
1
6 2
..
##
##
#.
..
.#
'''
# output Forfeit
