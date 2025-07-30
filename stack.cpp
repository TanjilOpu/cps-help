#include <iostream>
using namespace std;

#define MAX 100  // maximum size of stack

int stack[MAX];
int top = -1;  // stack is initially empty

// Push operation
void push(int x) {
    if (top >= MAX - 1) {
        cout << "Stack overflow! Cannot push " << x << endl;
        return;
    }
    top++;
    stack[top] = x;
    cout << "Pushed " << x << " onto the stack.\n";
}

// Pop operation
void pop() {
    if (top == -1) {
        cout << "Stack underflow! Cannot pop.\n";
        return;
    }
    cout << "Popped " << stack[top] << " from the stack.\n";
    top--;
}

// Display operation
void display() {
    if (top == -1) {
        cout << "Stack is empty.\n";
        return;
    }
    cout << "Stack elements from top to bottom:\n";
    for (int i = top; i >= 0; i--) {
        cout << stack[i] << endl;
    }
}

int main() {
    // Sample operations
    push(10);
    push(20);
    push(30);
    display();

    pop();
    display();

    return 0;
}
