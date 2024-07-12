// n:5
// *****
// ****
// ***
// **
// *

#include <iostream>
using namespace std;

int main()
{
   int n,i,j;
   
     cout << "n:" ;
     cin>> n ;
     for(i=1;i<=n;i++)
     {
        //print space
        for(j=1;j<=n-i+1;j++)
        { 
        cout << "*";
     }
     cout << endl;
     }
}