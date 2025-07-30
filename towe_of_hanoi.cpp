#include <iostream>
using namespace std;

// Recursive function to solve Tower of Hanoi
void towerOfHanoi(int n, char source, char helper, char destination) {
    if (n == 1) {
        cout << "Move disk 1 from " << source << " to " << destination << endl;
        return;
    }

    // Move top n-1 disks from source to helper using destination as temporary
    towerOfHanoi(n - 1, source, destination, helper);

    // Move the nth disk from source to destination
    cout << "Move disk " << n << " from " << source << " to " << destination << endl;

    // Move the n-1 disks from helper to destination using source as temporary
    towerOfHanoi(n - 1, helper, source, destination);
}

int main() {
    int n;
    cout << "Enter number of disks: ";
    cin >> n;

    // A, B, C are the rod names
    towerOfHanoi(n, 'A', 'B', 'C');

    return 0;
}
