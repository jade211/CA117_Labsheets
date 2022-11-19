#!/usr/bin/env python3

import sys
class Graph(object):

    def __init__(self, V):
       self.adj = {}  # used to map vertices to their neighbours (nodes)
       self.V = V  # number of vertices (numbers in graph, eg 7)
       for v in range(V):  # for number in range 0-7
          self.adj[v] = list()  # makes empty list mapped to vertices (because we dont know what nodes are connected to what vertices, have not added yet)

    def addEdge(self, v, w):  # goes into file and goes line by line grabbing v w (0 1) (4 2) etc
       self.adj[v].append(w)  # if v is connected to w, w is also connected to v
       self.adj[w].append(v)  # both get added to lists we created above for each vertice


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
      if self.visited[v] is True:  # is in a pathway to another vertice (not out on own)
         return True
      else:
         return False

   def pathTo(self, v):
      if self.hasPathTo(v) is False:
         return None
      path = [v]
      while v != self.s:
         v = self.parent[v]
         path.append(v)
      return path[::-1]


def main():
    with open('graph01.txt') as f:
       V = int(f.readline())
       g = Graph(V)

       print(g.adj)  # empty dictionary mapping (nothing added yet except empty list)

       for line in f:
          v, w = [int(t) for t in line.strip().split()]
          g.addEdge(v, w)  # using addEdge method to map

       print(g.adj)  # now has mapping complete

    paths = DFSPaths(g, 0)

    print(paths.hasPathTo(6))
    print(paths.pathTo(6))


if __name__ == '__main__':
   main()
