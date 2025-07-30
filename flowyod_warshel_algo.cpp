#include <iostream>
using namespace std;

const int INF = 1e9;
const int N = 100;
int dist[N][N];

int main() {
    int n;
    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter adjacency matrix (INF=99999 for no edge):\n";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> dist[i][j];

    // Floyd–Warshall
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];

    cout << "All pairs shortest path matrix:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            cout << (dist[i][j] >= INF ? -1 : dist[i][j]) << " ";
        cout << endl;
    }

    return 0;
}
