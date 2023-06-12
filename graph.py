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
    
g = graph()
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,4)
print(g.get_v())
print(g.get_edge())