#!/usr/bin/env python3

import sys

class Graph(object):

    def __init__(self, V):
        self.adj = {}
        self.V = V
        for v in range(V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

class DFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False for _ in range(g.V)]
        self.parent = [False for _ in range(g.V)]
        self.dfs(s)

    def dfs(self, v):
        self.visited[v] = True
        for w in self.g.adj[v]:
            if not self.visited[w]:
                self.parent[w] = v
                self.dfs(w)

    def hasPathTo(self, v):
        return self.visited[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = []
        while v is not False:
            path.insert(0, v)
            v = self.parent[v]
        return path


lines = sys.stdin.readlines()
V = int(lines[0])
islands = Graph(V)
for line in lines[1:]:
   v, w = [int(t) for t in line.strip().split()]
   islands.addEdge(v, w)

num = 0
visited = []
for i in range(V):
   if i not in visited:
      paths = DFSPaths(islands, i)
      for j in range(V):
         if j not in visited and paths.hasPathTo(j):
            visited.append(j)
      num = num + 1
print(num)
