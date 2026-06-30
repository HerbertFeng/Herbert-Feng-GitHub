'''
@Project : Class
@File : Motorcycle Meeting Madness (AIPO).py
@Author : Herbert
@Date : 2/15/2024 6:04 PM
'''
import heapq
from collections import defaultdict

'''
1 Motorcycle Meeting Madness
In Ireland there exists a clandestine network of motorcycle gangs. These gangs like
to convene and share their motorcycle gang ideas. Unfortunately, fuel is expensive
and even the motorcycle gangs are affected by the tough economic climate. The
motorcycle gangs need your help to save money. Your task, should you choose to
accept it, is to identify a common location where the gangs can convene such that
their total fuel bill will be minimized.
Given a set of locations L, a set of links between these locations, and a set of
motorcycle gangs G of varying sizes at some locations in L, find the location which
has the lowest fuel cost for all groups to travel to. All members of a gang start in
the same location and they each travel on their own motorcycle and all members of
a group must travel the same route. The cost for a group to travel a route is the
number of gang members times the fuel cost for that route.
Input
First line of input contains 3 space-separated integers n, e and g, with 2 ≤ n < 150,
n ≤ e < 2500, and 1 ≤ g < n. The integer n is the number of locations that the
gangs are aware of. To keep the locations of their meetings secret, the gangs have
given each location an integer identifier starting from zero. e is the number of links
between locations, and g is the number of groups.
The next e lines each contain 3 space-separated integers a, b and f, with 0 ≤
a, b < n, a != b, and 0 < f ≤ 10. This means there is a bi-directional link between
secret locations a and b with a fuel cost of f.
The following g lines each contain 2 space-separated integers c, d, with 0 ≤ c <
n, and 0 < d ≤ 50. This describes a motor cycle gang at a secret location c of size
d.
Output
Your program should output a line containing two space-separated integers, i and
c. i is the identifier of the secret location that all gangs should travel to, which has
the lowest cost to travel to. c is the total cost for all groups to travel to location i.
This line should be follow by a single new line character.

Sample Input 1
5 8 4
0 1 2
0 4 2
0 2 1
1 2 1
1 3 3
2 3 1
2 4 1
3 4 2
0 3
1 3
3 3
4 4
Sample Output 1
2 13

Sample Input 2
6 7 5
0 1 3
0 2 1
1 5 4
2 3 1
2 4 2
3 5 6
4 5 3
1 6
2 1
3 3
4 2
5 4
Sample Output 2
1 47
'''
def shortestPath(n, start,adj):
    distance = [float('inf')] * n
    distance[start] = 0

    heap = [(0, start)]

    while heap:
        cost, node = heapq.heappop(heap)

        for n2, cur_cost in adj[node]:
            if distance[n2] > cur_cost + cost:
                distance[n2] = cur_cost + cost
                heapq.heappush(heap, (cur_cost + cost, n2))

    return distance

def main():
    n,nlinks,ngangs = map(int,input().split())
    adj = defaultdict(list)
    for _ in range(nlinks):
        n1,n2,cost = map(int,input().split())
        adj[n1].append((n2,cost))
        adj[n2].append((n1, cost))

    gangs = [0] * n
    for _ in range(ngangs):
        loc,size = map(int,input().split())
        gangs[loc] = size

    meet,cost = 0,float('inf')
    for i in range(n):
        lst = shortestPath(n,i,adj)
        total_cost = 0
        for j in range(len(gangs)):
            total_cost += gangs[j]*lst[j]
        if total_cost<cost:
            meet = i
            cost = total_cost
    print('{} {}'.format(meet,cost))

main()



