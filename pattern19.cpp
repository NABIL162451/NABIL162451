// n:4
// D 
// C D
// B C D
// A B C D

#include <iostream>
using namespace std;

int main()
{
   int n,i,j;

     cout << "n:" ;
     cin>> n ;
     for(i=1;i<=n;i++)
     {
        char ch = 'A'+n-i;
     for(j=1;j<=i;j++)
     {
     cout << ch << ' ';
     ch=ch+1;
     }
     cout << endl;
     }
}