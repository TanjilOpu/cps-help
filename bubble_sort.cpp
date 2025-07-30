#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    vector<int>v(n);
    for(int i=0;i<n;i++) cin>>v[i];
    
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n-i;j++)
        {
            if(v[j]>v[j+1])
            {
                swap(v[j],v[j+1]);
            }
        }
    }
    for(auto it:v) cout<<it<<" ";
    cout<<endl;
}