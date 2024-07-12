// n:5
// *****
// ****
// ***
// **
// *
// **
// ***
// ****
// *****
#include <iostream>
using namespace std;

int main()
{
    int n,i,j;

    cout << "n:";
    cin>> n;

     for(i=1;i<n;i++)
    {
        for(j=1;j<=n-i+1;j++)
        {
            cout << "*";
        }
        // for(i=1;i<=n;i++){}
        cout <<endl;
    }
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=i;j++)
        {
            cout << "*";
        }
        // for(i=1;i<=n;i++){}
        cout <<endl;
    }
   
    
}