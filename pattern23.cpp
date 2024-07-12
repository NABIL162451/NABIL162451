// n:5
//     *
//    **
//   ***
//  ****
// *****

#include <iostream>
using namespace std;

int main()
{
   int n,i,j,k;
   
     cout << "n:" ;
     cin>> n ;
     for(i=1;i<=n;i++)
     {
        //print space
        for(j=1;j<=n-i;j++)
        { 
        cout << " ";
        }
        for(k=1;k<=i;k++)
        {
        cout << '*';
     }
     cout << endl;
     }
}