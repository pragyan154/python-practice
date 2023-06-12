# dfs on undirected graph

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

    def get_v(self):
        return list(self.graph.keys())
    
    def get_edge(self):
        edges = []
        for v in self.graph:
            for neighbor in self.graph[v] :
                edges.append((v,neighbor))

        return edges
    

#--------------------------------------------------
    def dfs(self, start):
        done = set()

        def dfs_itr(vertex):
            done.add(vertex)
            print(vertex, end=" ")
            
            
            for neighbour in self.graph[vertex]:
                if neighbour not in done:
                    dfs_itr(neighbour)

        dfs_itr(start)
    
# -------------------------------------------------
g = graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

# Perform DFS traversal
print("DFS Traversal:")
g.dfs('A')