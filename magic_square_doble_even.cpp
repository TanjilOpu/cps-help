#include <iostream>
using namespace std;

const int MAX = 100;
int square[MAX][MAX];
int n;

void magicSquareDoublyEven() {
    int i, j;

    // Step 1: Fill with 1 to n*n
    int num = 1;
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            square[i][j] = num++;

    // Step 2: Invert the values at specific positions
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if ((i % 4 == j % 4) || ((i + j) % 4 == 3)) {
                square[i][j] = (n * n + 1) - square[i][j];
            }
        }
    }

    // Print the square
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            cout << square[i][j] << "\t";
        }
        cout << endl;
    }
}

int main() {
    cout << "Enter a doubly even number (n % 4 == 0): ";
    cin >> n;

    if (n % 4 != 0) {
        cout << "Only doubly even n is supported by this method.\n";
        return 0;
    }

    magicSquareDoublyEven();
    return 0;
}
