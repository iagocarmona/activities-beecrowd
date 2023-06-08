from queue import Queue

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
    
    def findShortestPathDFS(self, start, end):
        # Inicializa as variáveis de controle
        visited = set()
        parent = {}
        queue = Queue()
        queue.put(start)
        parent[start] = None

        # Executa a busca em largura
        while not queue.empty():
            current_vertex = queue.get()
            visited.add(current_vertex)
            if current_vertex == end:
                break
            for neighbor, _ in self.vertices[current_vertex].edges:
                if neighbor not in visited:
                    parent[neighbor] = current_vertex
                    queue.put(neighbor)

        # Monta o caminho percorrido
        path = []
        current_vertex = end
        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = parent[current_vertex]
        path.reverse()

        return path
        
graph = Graph(64)

# Adicionando arestas para o tabuleiro de xadrez
for row in range(8):
    for col in range(8):
        vertex = f"{chr(ord('a') + col)}{row + 1}"
        # Movimentos do cavalo
        possible_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        for move in possible_moves:
            new_col = col + move[0]
            new_row = row + move[1]
            if 0 <= new_col < 8 and 0 <= new_row < 8:
                neighbor = f"{chr(ord('a') + new_col)}{new_row + 1}"
                graph.addEdge(vertex, neighbor)   
    
while True:
    try:
        start, destination = input().split()
    except:
        break
    
    shortestPath = graph.findShortestPathDFS(start, destination)
    
    print(f"To get from {start} to {destination} takes {len(shortestPath)-1} knight moves.")

