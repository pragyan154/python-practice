from collections import deque
# class graph:
#     def __init__(self):
#         self.graph = {}

#     def add_edge(self, source, destination):
#         if source in self.graph:
#             self.graph[source].append(destination)
#         else:
#             self.graph[source] = [destination]


#     def bfs(self,start):
#         visitedd = set()

#         queue = deque()

#         visitedd.add(start)
#         queue.append(start)

#         while queue:
#             current = queue.popleft()
#             print(current, end="->")

#             if current in self.graph:
#                 for adj_vertices in self.graph[current]:
#                     if adj_vertices not in visitedd:
#                         visitedd.add(adj_vertices)
#                         queue.append(adj_vertices)

class graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self,v1,v2):
        if v1 not in self.graph:
            self.add_vertex(v1)

        if v2 not in self.graph:
            self.add_vertex(v2)

        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def bfs(self,start):
        visitedd = set()

        queue = deque()

        visitedd.add(start)
        queue.append(start)

        while queue:
            current = queue.popleft()
            print(current, end="->")

            if current in self.graph:
                for adj_vertices in self.graph[current]:
                    if adj_vertices not in visitedd:
                        visitedd.add(adj_vertices)
                        queue.append(adj_vertices)

    def get_edge(self):
        edges = []
        for v in self.graph:
            for neighbor in self.graph[v] :
                edges.append((v,neighbor))

        return edges
    

g = graph()
g.add_edge('A', 'C')
g.add_edge('A', 'B')
g.add_edge('A', 'D')
g.add_edge('D', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'G')


print("BFS Traversal:")
g.bfs('A')
print(g.get_edge())

# def bfs(self,src):
#         visited = set()
#         queue = []
#         queue.append(src)
#         visited.add(src)
#         while len(queue):
#             size = len(queue)
#             for i in range(size):
#                 front = queue.pop(0)
#                 print(front,end=" ")
#                 for j in self.graph[front]:
#                     if j not in visited:
#                         queue.append(j)
#                         visited.add(j)
#             print()