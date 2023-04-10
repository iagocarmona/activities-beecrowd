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
        self.result = 0

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
        
    def bfs(self, start_vertex, target_vertex):
        visited = set()
        queue = [(start_vertex, 0)]

        while queue:
            vertex, depth = queue.pop(0)
            if vertex not in visited:
                if vertex != start_vertex:
                    visited.add(vertex)
                if vertex == target_vertex:
                    return depth
                try:
                    for edge in self.vertices[vertex].edges:
                        neighbor, _ = edge
                        if neighbor not in visited:
                            queue.append((neighbor, depth + 1))
                except:
                    break


while True:
    AmountPoints, amountConections = map(int, input().split())
    
    if AmountPoints < 4 or AmountPoints > 4000 or amountConections < 5 or amountConections > 5000:
        break
    
    g = Graph(AmountPoints)

    while amountConections > 0:
        X, Y = map(str,input().split())
        
        g.addEdge(X, Y)
        
        amountConections -= 1   
        
    result1 = g.bfs("Entrada","*")
    result2 = g.bfs("*","Saida")
    
    if result1 is not None and result2 is not None:
        print(result1 + result2)

    break
