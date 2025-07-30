#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<double> value;
vector<double> weight;

// Pair of index and value-to-weight ratio
bool cmp(int i, int j) {
    return (value[i] / weight[i]) > (value[j] / weight[j]);
}

double fractionalKnapsack(int capacity, int n) {
    vector<int> idx(n);
    for (int i = 0; i < n; i++) idx[i] = i;

    sort(idx.begin(), idx.end(), cmp); // Sort indices by ratio
      for(auto it:idx) cout<<it <<" ";
      cout<<endl;
    double totalValue = 0.0;

    for (int i = 0; i < n; i++) {
        int k = idx[i];
        if (capacity >= weight[k]) {
            totalValue += value[k];
            capacity -= weight[k];
        } else {
            totalValue += value[k] * (capacity / weight[k]);
            break;
        }
    }

    return totalValue;
}

int main() {
    int n, capacity;
    cout << "Enter number of items: ";
    cin >> n;

    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    value.resize(n);
    weight.resize(n);

    cout << "Enter value and weight of each item:\n";
    for (int i = 0; i < n; i++) {
        cin >> value[i] >> weight[i];
    }

    double result = fractionalKnapsack(capacity, n);
    cout << "Maximum value in knapsack = " << result << endl;

    return 0;
}
