# 1469 - Chefe

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
    
    def invertEdges(self):
        inverted_edges = []

        # Percorre todas as arestas existentes e as inverte
        for vertex_name in self.vertices:
            vertex = self.vertices[vertex_name]
            for edge in vertex.edges:
                neighbor = edge[0]
                inverted_edges.append((neighbor, vertex_name))

        # Remove todas as arestas existentes
        for vertex_name in self.vertices:
            vertex = self.vertices[vertex_name]
            vertex.edges = []

        # Adiciona as arestas invertidas
        for edge in inverted_edges:
            vertex_name, neighbor = edge
            self.addEdge(vertex_name, neighbor)
    
    def changeVertex(self, left, right):
        vertex_aux = self.vertices[left]
        left_aux_edges = self.vertices[left].edges
        right_aux_edges = self.vertices[right].edges
        
        self.vertices[left] = self.vertices[right]
        self.vertices[left].edges = left_aux_edges
        
        self.vertices[right] = vertex_aux
        self.vertices[right].edges = right_aux_edges
    
    def searchMinAgeManager(self, left):
        queue = [left]
        visited = set(queue)
        min_age = float('inf')

        self.invertEdges()

        while queue:
            current = queue.pop(0)
            if current in self.vertices:
                vertex = self.vertices[current]
                if vertex.age < min_age:
                    min_age = vertex.age

                for edge in vertex.edges:
                    neighbor = edge[0]
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

        self.invertEdges()

        if min_age == float('inf'):
            return "*"
        else:
            return min_age
    
    def printGraph(self):
        for vertex_name in self.vertices:
            vertex = self.vertices[vertex_name]
            print(f"Vertex {vertex_name}, {vertex.age}:")
            for edge in vertex.edges:
                print(f"  -> {edge[0]}")

while True: 
    try:
        N, M, I = map(int, input().split())
    except:
        break
    
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
    
    while I > 0:
        strInput = input().split()
        
        instruction = strInput[0]
        left = int(strInput[1])
        
        if len(strInput) == 3:
            right = int(strInput[2])
                    
        if instruction == 'T':
            g.changeVertex(left, right)
            g.printGraph()
            
        if instruction == 'P':
            min_age = g.searchMinAgeManager(left)
            print(min_age)
        
        I = I - 1
