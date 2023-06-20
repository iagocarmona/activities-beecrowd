class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def addEdge(self, vertex, weight=0):
        self.edges.append((vertex, weight))


class Graph:
    def __init__(self, num_vertices):
        self.vertices = {}
        self.num_vertices = num_vertices

    def addVertex(self, vertex):
        new_vertex = Vertex(vertex)
        self.vertices[vertex] = new_vertex

    def addEdge(self, vertex1, vertex2, weight=0):
        if vertex1 not in self.vertices:
            self.addVertex(vertex1)
        if vertex2 not in self.vertices:
            self.addVertex(vertex2)
        
        self.vertices[vertex1].addEdge(vertex2, weight)
        self.vertices[vertex2].addEdge(vertex1, weight)
        
    def printGraph(self):
        for vertex_name in self.vertices:
            vertex = self.vertices[vertex_name]
            print(f"Vertex {vertex_name}:")
            for edge in vertex.edges:
                print(f"  -> {edge[0]} (weight={edge[1]})")
    
    def find_minimum_spanning_tree(self):
        start_vertex = list(self.vertices.keys())[0]
        visited = {start_vertex}  # Conjunto de vértices visitados
        minimum_spanning_tree = Graph(len(self.vertices))

        while len(visited) < len(self.vertices):
            min_weight = float('inf')
            min_edge = None

            # Percorrer todos os vértices visitados e encontrar a aresta de menor peso
            for vertex in visited:
                for neighbor, weight in self.vertices[vertex].edges:
                    if neighbor not in visited and weight < min_weight:
                        min_weight = weight
                        min_edge = (vertex, neighbor, weight)

            # Adicionar a aresta de menor peso à árvore geradora mínima
            vertex1, vertex2, weight = min_edge
            minimum_spanning_tree.addEdge(vertex1, vertex2, weight)

            # Marcar o vértice vizinho como visitado
            visited.add(vertex2)

        return minimum_spanning_tree
    
    def get_unique_edges(self):
        unique_edges = set()

        for vertex_name in self.vertices:
            vertex = self.vertices[vertex_name]
            for edge in vertex.edges:
                edge_tuple = (min(vertex_name, edge[0]), max(vertex_name, edge[0]), edge[1])
                unique_edges.add(edge_tuple)

        return unique_edges
        
        
num_testes = 1
        
while True:
    input_values = input().split()
    
    if len(input_values) >= 2:
        N, M = map(int, input_values)
    else:
        break
    
    if N == 0:
        break
    
    g = Graph(N)
    
    while M > 0:
        X, Y, Z = map(int, input().split())
        g.addEdge(X, Y, Z)
        M -= 1
    
    print("Teste", num_testes)
    mst = g.find_minimum_spanning_tree()
    unique_edges = mst.get_unique_edges()
    
    # Imprimir as arestas no formato desejado
    for edge in unique_edges:
        vertex1, vertex2, weight = edge
        print(f"{vertex1} {vertex2}")
        
    print("\n", end="")
    
    num_testes += 1
        