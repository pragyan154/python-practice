class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination):
        if source in self.graph:
            self.graph[source].append(destination)
        else:
            self.graph[source] = [destination]

    def print_graph(self):
        for vertex in self.graph:
            connections = "->".join(self.graph[vertex])
            print(vertex, "->", connections)


graph = Graph()

graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'A')

# Print the graph
graph.print_graph()
