#!/usr/bin/env python3

import sys

def IfPath(k, v):
    return k in g.adj[v]

def add_island(islands, k, v):
    v.append(k)
    islands.append(v)
    return islands


class Graph(object):

   def __init__(self, V):
      self.V = V
      self.adj = {}
      for v in range(V):
         self.adj[v] = list()

   def addEdge(self, v, w):
      self.adj[v].append(w)
      self.adj[w].append(v)


info = sys.stdin.readlines()
vertices = int(info[0])
lines = info[1:]

g = Graph(vertices)
for line in lines:
   v, w = [int(t) for t in line.strip().split()]
   g.addEdge(v, w)

islands = []
for key, value in g.adj.items():
    HasPath = False
    for island in islands:
        for j in island:
            if IfPath(key, j):
                HasPath = True
                break
    if not HasPath:
        islands = add_island(islands, key, value)
    if len(islands) == 0:
        islands = add_island(islands, key, value)

print(len(islands))
# print(g.adj)
