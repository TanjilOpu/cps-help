#include <iostream>
using namespace std;

int n;
int square[101][101]; // global array

void magicSquare() {
    if (n % 2 == 0) {
        cout << "n is even" << endl;
        return;
    }

    // Initialize the square to 0
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            square[i][j] = 0;

    int i = 0;
    int j = (n - 1) / 2;

    square[i][j] = 1;

    for (int key = 2; key <= n * n; key++) {
        int k, l;

        // Compute next row (k)
        if (i > 0)
            k = i - 1;
        else
            k = n - 1;

        // Compute next column (l)
        if (j > 0)
            l = j - 1;
        else
            l = n - 1;

        if (square[k][l] == 0) {
            i = k;
            j = l;
        } else {
            i = (i + 1) % n;
            // j remains the same
        }

        square[i][j] = key;
    }

    // Print the magic square
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << square[i][j] << "  ";
        }
        cout << endl;
    }
}

int main() {
    cout << "Enter an odd value for n: ";
    cin >> n;
    magicSquare();
    return 0;
}

/*[6 1 8]
[7 5 3]
[2 9 4]
*/
