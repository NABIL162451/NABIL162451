// n:5
// ********************
// ********    ********
// ******        ******
// ****            ****
// **                **
// ****            ****
// ******        ******
// ********    ********
// ********************
#include <iostream>
using namespace std;

int main()
{
    int n,i,j,k;

    cout << "n:";
    cin>> n;

     for(i=1;i<n;i++)
    {
        for(j=1;j<=n-i+1;j++)
        {
            cout << "**";
        }
        for(k=1;k<=i-1;k++)
        {
                cout << "  ";
        }
        for(j=1;j<=i-1;j++)
        {
            cout << "  ";
        }
        for(k=1;k<=n-i+1;k++)
        {
                cout << "**";
        }
        cout << endl;
    }
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=i;j++)
        {
            cout << "**";
        }
        for(k=1;k<=n-i;k++)
        {
                cout << "  ";
        }
        for(j=1;j<=n-i;j++)
        {
            cout << "  ";
        }
        for(k=1;k<=i;k++)
        {
                cout << "**";
        }
        // for(i=1;i<=n;i++){}
        cout <<endl;
    }
   
    
}