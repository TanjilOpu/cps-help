#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n; // number of nodes
vector<int> adj[100]; // adjacency list
vector<bool> visited(100, false); // visited array for DFS

void dfs(int node) {
    visited[node] = true;
    cout << node << " ";

    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor);
        }
    }
}

void bfs(int start) {
    vector<bool> visited_bfs(n, false); // separate visited for BFS
    queue<int> q;

    visited_bfs[start] = true;
    q.push(start);

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int neighbor : adj[node]) {
            if (!visited_bfs[neighbor]) {
                visited_bfs[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

int main() {
    int edges;
    cin >> n >> edges;

    // Input edges
    for (int i = 0; i < edges; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u); // undirected
    }

    cout << "DFS from node 0: ";
    dfs(0);
    cout << endl;

    cout << "BFS from node 0: ";
    bfs(0);
    cout << endl;

    return 0;
}
