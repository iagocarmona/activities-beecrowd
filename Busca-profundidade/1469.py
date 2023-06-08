class Vertex:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.edges = []

    def addEdge(self, vertex, weight=0):
        self.edges.append((vertex, weight))

class Graph:
    def __init__(self, num_vertices):
        self.vertices = {}
        self.num_vertices = num_vertices

    def addVertex(self, vertex, age):
        new_vertex = Vertex(vertex, age)
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

while True: 
    N, M, I = map(int, input().split())
    
    if N < 1 or N > 500:
        break
    if M < 0 or M > 60 * (10*10*10):
        break
    if I < 1 or I > 500:
        break
    
    strAges = input().split()
    
    if len(strAges) < N or len(strAges) > N:
        break
    
    intAges = []
    for i in strAges:
        intAges.append(int(i))
    
    g = Graph(N)
    
    idx = 1
    for age in intAges:
        g.addVertex(idx, age)
        idx = idx + 1
        
    edgesCount = 0
    while edgesCount < M:
        X, Y = map(int, input().split())
        g.addEdge(X,Y)
        edgesCount = edgesCount + 1
    
    g.printGraph()
        
