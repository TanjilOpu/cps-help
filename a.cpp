#include <bits/stdc++.h>
using namespace std;
const int maxi = 100;
int stak[maxi];
int top = -1;
void push(int n)
{
    if (top >= maxi - 1)
    {
        cout << "stack overflow\n";
        return;
    }
    top++;
    stak[top] = n;
}
void display()
{
    if (top < 0)
    {
        cout << "Underflow\n";
        return;
    }
   for(int i=top;i>=0;i--)
   {
    cout<<stak[i]<<endl;
   }
}
void pop()
{
    if(top<0)
    {
        cout<<"Stack is empthy\n";
        return;
    }
    cout<<"poped value " <<stak[top]<<endl;
    top--;
}
int main()
{
    push(10);
    push(20);
    push(30);
    display();
    pop();
    display();
}