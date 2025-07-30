#include <iostream>
#include <vector>
using namespace std;

vector<int> v; // Global vector

// Partition function using pivot = v[low]
int partition(int low, int high) {
    int pivot = v[low];
    int i = low + 1;
    int j = high;

    while (i <= j) {
        while (i <= high && v[i] <= pivot) i++;
        while (v[j] > pivot) j--;

        if (i < j)
            swap(v[i], v[j]);
    }
    swap(v[low], v[j]); // Place pivot in its correct position
    return j;
}

// Quicksort function
void quicksort(int low, int high) {
    if (low < high) {
        int pi = partition(low, high);
        quicksort(low, pi - 1);
        quicksort(pi + 1, high);
    }
}

// Main function
int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    v.resize(n);
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) cin >> v[i];

    quicksort(0, n - 1);

    cout << "Sorted array: ";
    for (int x : v) cout << x << " ";
    cout << endl;

    return 0;
}
