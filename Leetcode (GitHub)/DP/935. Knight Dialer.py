'''
@Project : Class
@File : 935. Knight Dialer.py
@Author : Herbert
@Date : 11/28/2023 12:09 AM
'''


class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        neighbors = {

            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (0, 3, 9),
            5: (),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)

        }

        current_count = [1] * 10
        for _ in range(n - 1):
            next_count = [0] * 10
            for in_key in range(10):
                for out_key in neighbors[in_key]:
                    next_count[out_key] = (next_count[out_key] + current_count[in_key]) % (10 ** 9 + 7)
            current_count = next_count

        return sum(current_count) % (10 ** 9 + 7)

        '''
        def Solution_with_cache(start,n):
            cache = {}
            def dfs(start,n):
                if (start,n) in cache:
                    return cache[(start,n)]

                if n==0:
                    return 1

                num_seq = 0 
                for nei in neighbors[start]:
                    num_seq = (num_seq + dfs(nei, n-1))% (10**9 + 7)
                    cache[(nei, n)] = num_seq
                return num_seq

            return dfs(start,n)

        ans = 0
        for i in range(10):
            ans+= (Solution_with_cache(i,n-1))% (10**9 + 7)
        return ans% (10**9 + 7)
        '''



