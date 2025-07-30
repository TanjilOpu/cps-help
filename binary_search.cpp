#include <iostream>
#include <vector>
using namespace std;

vector<int> v; // global vector
int n;         // global size

int binarySearch(int key) {
    int low = 0, high = n - 1;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (v[mid] == key)
            return mid; // found
        else if (v[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return -1; // not found
}

int main() {
    cin >> n;
    v.resize(n);

    for (int i = 0; i < n; i++)
        cin >> v[i]; // input must be sorted

    int key;
    cin >> key;

    int index = binarySearch(key);

    if (index != -1)
        cout << "Found at index: " << index << endl;
    else
        cout << "Not found" << endl;

    return 0;
}
