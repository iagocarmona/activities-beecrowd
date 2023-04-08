# Pedágio
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
        self.result = []

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
        
    def bfs_limited(self, start_vertex, limit):
        visited = set()
        queue = [(start_vertex, 0)]
        self.result = []
        
        while queue:
            vertex, depth = queue.pop(0)
            if depth > limit:
                break
            if vertex not in visited:
                if vertex != start_vertex:
                    visited.add(vertex)
                    self.result.append(vertex)
                try:
                    for edge in self.vertices[vertex].edges:
                        neighbor, _ = edge
                        if neighbor not in visited:
                            queue.append((neighbor, depth + 1))
                except:
                    break
    
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def printArray(arr):
    idx = 0
    for i in arr:
        if idx < len(arr) - 1:
            print(i, end = ' ')
        else:
            print(i, end='')
        idx += 1
    
numOfTests = 0

while True:
    C, E, L, P = map(int, input().split())
    
    if C == E == L == P == 0:
        break
    
    g = Graph(C)
    
    numOfTests += 1    
    
    while E > 0:
        X, Y = map(int, input().split())
        
        if X and Y > C or X and Y < 1:
            break
        
        g.addEdge(X, Y)
        
        E -= 1
        
    print("Teste", numOfTests)
    g.bfs_limited(L,P)
    result = quick_sort(g.result)
    printArray(result)
    print("\n")
        
    
    