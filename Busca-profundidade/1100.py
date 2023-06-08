# MOVIMENTOS DO CAVALO

#include <iostream>
#include <unordered_map>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

class Vertex {
public:
    string name;
    vector<pair<string, int>> edges;

    Vertex(string n) {
        name = n;
    }

    void addEdge(string vertex, int weight) {
        edges.push_back(make_pair(vertex, weight));
    }
};

class Graph {
public:
    unordered_map<string, Vertex*> vertices;

    void addVertex(string name) {
        if (vertices.find(name) == vertices.end()) {
            vertices[name] = new Vertex(name);
        }
    }

    void addEdge(string v1, string v2, int weight) {
        addVertex(v1);
        addVertex(v2);
        vertices[v1]->addEdge(v2, weight);
        vertices[v2]->addEdge(v1, weight);
    }

    vector<string> findShortestPathBFS(string start, string end) {
        unordered_map<string, bool> visited;
        unordered_map<string, string> parent;
        queue<string> q;
        vector<string> path;

        q.push(start);
        visited[start] = true;
        parent[start] = "";
        while (!q.empty()) {
            string curr = q.front();
            q.pop();
            if (curr == end) {
                while (curr != "") {
                    path.push_back(curr);
                    curr = parent[curr];
                }
                break;
            }
            for (auto neighbor : vertices[curr]->edges) {
                string neighbor_name = neighbor.first;
                if (!visited[neighbor_name]) {
                    visited[neighbor_name] = true;
                    parent[neighbor_name] = curr;
                    q.push(neighbor_name);
                }
            }
        }
        reverse(path.begin(), path.end());
        return path;
    }
};

int main() {
    Graph graph;
    // Adicionando arestas para o tabuleiro de xadrez
    for (int row = 0; row < 8; row++) {
        for (int col = 0; col < 8; col++) {
            string vertex = string(1, char('a' + col)) + to_string(row + 1);
            // Movimentos do cavalo
            vector<pair<int, int>> possible_moves = {
                {2, 1}, {2, -1}, {-2, 1}, {-2, -1},
                {1, 2}, {1, -2}, {-1, 2}, {-1, -2}
            };
            for (auto move : possible_moves) {
                int new_col = col + move.first;
                int new_row = row + move.second;
                if (new_col >= 0 && new_col < 8 && new_row >= 0 && new_row < 8) {
                    string neighbor = string(1, char('a' + new_col)) + to_string(new_row + 1);
                    graph.addEdge(vertex, neighbor, 1);
                }
            }
        }
    }

    string start, destination;
    while (cin >> start >> destination) {
        auto shortestPath = graph.findShortestPathBFS(start, destination);

        cout << "To get from " << start << " to " << destination << " takes " << shortestPath.size()-1 << " knight moves." << endl;
    }
    return 0;
}
