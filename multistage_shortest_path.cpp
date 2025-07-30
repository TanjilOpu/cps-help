#include <iostream>
#include <climits>
using namespace std;

const int N = 100;
int graph[N][N];
int cost[N];
int path[N];

int main() {
    int n;
    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter adjacency matrix (0 for no edge):\n";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> graph[i][j];

    cost[n - 1] = 0; // Destination cost is 0

    for (int i = n - 2; i >= 0; i--) {
        cost[i] = INT_MAX;
        for (int j = i + 1; j < n; j++) {
            if (graph[i][j]) {
                if (cost[i] > graph[i][j] + cost[j]) {
                    cost[i] = graph[i][j] + cost[j];
                    path[i] = j;
                }
            }
        }
    }

    cout << "Minimum cost from source to destination: " << cost[0] << endl;
    cout << "Path: ";
    int i = 0;
    while (i < n - 1) {
        cout << i << " -> ";
        i = path[i];
    }
    cout << n - 1 << endl;

    return 0;
}
