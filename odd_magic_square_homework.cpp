#include<bits/stdc++.h>
using namespace std;
int square[5][5];
void magic(int n)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            square[i][j]=0;
        }
    }

    int i=0;
    int j= n/2;

    int input  =9;
            square[i][j]=input;

    for(int key = 1;key<25;key++)
    {
        input++;

        int k,l;
        k = (i-1+n)%n;
        l = (j+1)%n;
        if(square[k][l]==0)
        {
            i = k;
            j = l;
        }
        else i = (i+1)%n;
                square[i][j]=input;


    }
     for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cout<<square[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;

}

int main()
{
    magic(5);
}