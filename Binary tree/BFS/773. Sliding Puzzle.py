'''
@Project : Class
@File : 773. Sliding Puzzle.py
@Author : Herbert
@Date : 11/10/2023 8:20 PM
'''
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def generate_new_board(old_board, neighbors):
            zero_idx = old_board.index('0')
            new_boards = []
            board = list(old_board)
            for pos in neighbours[zero_idx]:
                board[zero_idx], board[pos] = board[pos], board[zero_idx]
                new_boards.append(''.join(board))
                board[zero_idx], board[pos] = board[pos], board[zero_idx]
            return new_boards

        neighbours = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        start_board = ''.join([''.join(map(str, row)) for row in board])
        target_board = '123450'
        visited = {start_board}
        queue = [start_board]
        min_step = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                cur_board = queue.pop(0)
                if cur_board == target_board:
                    return min_step
                for new_board in generate_new_board(cur_board, neighbours):
                    if new_board not in visited:
                        queue.append(new_board)
                        visited.add(new_board)
            min_step += 1
        return -1
