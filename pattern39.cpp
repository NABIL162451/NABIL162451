#include <iostream>
using namespace std;

int main()
{
    int i,j,k,n;
    cout << "n: ";
    cin >> n;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n-i;j++)
        {
           cout << " ";
        }
        for(k=1;k<=i;k++)
        {
            if(i==n || k==1 || k==i )
            cout << "*";
            else {
                cout <<" ";
            }
        }
        cout <<endl;
    }
    
}