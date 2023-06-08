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
        
    def DFS(self, vertex, visited, component):
        visited.add(vertex)
        component.add(vertex)
        for neighbor, _ in self.vertices[vertex].edges:
            if neighbor not in visited:
                self.DFS(neighbor, visited, component)

    def findComponents(self):
        visited = set()
        components = []
        for vertex in self.vertices:
            if vertex not in visited:
                component = set()
                self.DFS(vertex, visited, component)
                components.append(component)
        # Adicionar vértices isolados como componentes
        for vertex in self.vertices:
            if vertex not in visited:
                component = set()
                component.add(vertex)
                components.append(component)
        num_components = len(components)
        return components, num_components

numOfTests = 0
N = int(input())

while True:
    if(numOfTests == N):
        break
    
    V, E = map(int, input().split())
    
    vertices = ['a', 'b', 'c','d', 'e', 'f','g', 'h', 'i','j', 'k', 'l','m', 'n', 'o','p', 'q', 'r','s', 't', 'u','v', 'w', 'x','y', 'z']
    
    g = Graph(V)
    
    idx = 0
    while V > 0:
        g.addVertex(vertices[idx])
        idx += 1
        V -= 1
    
    numOfTests += 1    
    
    while E > 0:
        X, Y = input().split()
        
        g.addEdge(X, Y)
        
        E -= 1
    print("Case #", end="")
    print(numOfTests, end="")
    print(":")
    components, num_components = g.findComponents()
    for item in components:
        sorted_list = sorted(item)
        print(",".join(sorted_list), end="")
        print(",")
    print(num_components, "connected components", end="\n\n")