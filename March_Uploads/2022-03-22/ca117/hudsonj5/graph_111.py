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

   def __init__(self, g, s):  # Gets given the graph from above and a starting node, starts at 2 (node) and searches g
      self.g = g
      self.s = s  # for each vertex, have i been there before. Can use a dictionary or a LIST. list of True or False. At index 1 (number indexes are numbers). will run from 0 - 6 (6 will actually be 7th vertex.)
    # For each vertex in the graph g, give me false
    # We have not visited anywhere yet
      self.visited = [False for _ in range(self.g.V)]  # self.g.V is just an integer, making range means 1-7
      self.parent = [False for _ in range(self.g.V)]
    # two things to remember during our dfs
    # where have i been (self.visited) so i dont go there again
    # how did i get there (self.parent)
      self.dfs(s)  # begins search from node s

   def dfs(self, v):
    # So we are exploring from v.
    # We are currently sitting at position v, vertex we are sitting on is green, we have ju
      self.visited[v] = True
    # where can i go next
    # lets consider each possible place i can go
      for w in self.g.adj[v]:
        # if i have not visited it then go there
         if not self.visited[w]:  # if self.visited[w] is False.
            # we are going to w from v, record it
             self.parent[w] = v  # recorded how got there. I am at w, got there from v
            # explore from vertex w
             self.dfs(w)

   def hasPathTo(self, v):
    # have you visited vertex v during your search
    # Return true if there is a path fropm s to v
    # during our search did we visit vertex v?
      return self.visited[v]  # will be True, if False, we didnt visit.

   def pathTo(self, v):
    # returns path from s to v (or none should one not exist)
      if not self.hasPathTo(v):
         return None
      path = [v]  # building path backwards, verified we visited v, building backards starting at v (back links).
    # v is where i am curently, not at s
      while v != self.s:  # v is where you currently are.
         v = self.parent[v]  # how you got to every vertex, how we got to v, takes you a step backwards, new v is back link
         path.append(v)  # eventually will break out of then when you are equal to s
      return path[::- 1]  # path is going from backwards to start so we need to reverse to fix.

def main():
   with open('graph01.txt') as f:

      V = int(f.readline())

      g = Graph(V)

      for line in f:
         v, w = [int(t) for t in line.strip().split()]
         g.addEdge(v, w)

      paths = DFSPaths(g, 0)
    # paths = DFSPaths(g, 4)

    # print(paths.visited)
    # print(paths.parent)

    # should print True
      print(paths.hasPathTo(6))
    # print(paths.hasPathTo(1))

    # Should print [0, 5, 3, 4, 6]
      print(paths.pathTo(6))
    # print(paths.PathTo(1)


if __name__ == '__main__':
   main()
