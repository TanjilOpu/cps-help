#include<bits/stdc++.h>
using namespace std;
int n;
vector<int>v;

void merge(int l1,int r1, int l2, int r2)
{
    vector<int>c;
    int i1=l1,i2=l2;
    while(i1<=r1 && i2<=r2)
    {
        if(v[i1]<=v[i2])
        {
            c.push_back(v[i1]);
            i1++;
        }
        else 
        {
            c.push_back(v[i2]);
            i2++;
        }
    }
    while(i1<=r1)
    {
        c.push_back(v[i1]);
        i1++;
    }
    
    while(i2<=r2)
    {
        c.push_back(v[i2]);
        i2++;
    }

    for(int i=0;i<c.size();i++)
    {
        v[l1+i]=c[i];
    }
}

void mergesort(int l,int r)
{
    // base case 
    if(l>=r)
    {
        return;
    }
    // function body
    int mid = (l+r)/2;
    mergesort(l,mid);
    mergesort(mid+1,r);

    merge(l,mid,mid+1,r);
}
int main()
{
    // cin>>n;
    // v.resize(n);
    int x;
   while(cin>>x)
    {
       v.push_back(x);
    }
    n=v.size();

    mergesort(0,n-1);
    for(auto it:v)
    {
        cout<<it<<" ";
    }
    cout<<endl;
}