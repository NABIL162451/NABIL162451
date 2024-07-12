// N:5
//     *
//    ***
//   *****
//  *******
// *********
//  *******
//   *****
//    ***
//     *
#include <iostream>
using namespace std;

int main()
{
    int n,i,j,k,l;
    cout << "N:";
    cin >> n;
    
for(i=1;i<n;i++)
    {
        for(j=1;j<=n-i;j++)
        {
            cout << " ";
        }
        for(k=1;k<=i-1;k++)
        {
            cout << "*";
        }
        for(l=1;l<=i;l++)
        {
            cout << "*";
        }
    cout << endl;
    }

for(i=1;i<=n;i++)
    {   
        for(j=1;j<=i-1;j++)
        {
            cout << " ";
        }
        for(k=1;k<=n-i+1;k++)
        {
            cout << "*";
        }
        for(l=1;l<=n-i;l++)
        {
            cout << "*";
        }
   cout <<endl; 
   }
}