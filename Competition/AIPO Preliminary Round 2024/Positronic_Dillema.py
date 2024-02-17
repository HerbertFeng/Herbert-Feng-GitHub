'''
@Project : Class
@File : Positronic_Dillema.py
@Author : Herbert
@Date : 1/11/2024 9:20 PM
'''


def travel(i, dic, start_lst):
    start = start_lst[i]
    end = dic[start]
    seen = set()
    while True:
        if end not in seen and end in dic:
            seen.add(end)
            end = dic[end]
            if start == end:
                return 'UNSAFE'
        else:
            return 'SAFE'


def main():
    dic = {}
    start_lst = []

    n = int(input())
    for i in range(n):
        a, b = map(int, input().split(','))

        dic[a] = b
        start_lst.append(a)

    flag = False
    for i in range(n):
        if travel(i, dic, start_lst) == 'UNSAFE':
            flag = True
            break

    if flag:
        print('UNSAFE')
    else:
        print('SAFE')


# Python program to detect cycle
# in a graph

from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be popped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in self.graph.keys():
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False




def mainv2():
    n=int(input())
    g=Graph(n)
    for i in range(n):
        a, b = map(int, input().split(','))
        g.addEdge(a,b)
    if g.isCyclic() == 1:
        print("UNSAFE")
    else:
        print("SAFE")

mainv2()



