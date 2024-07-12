// n:4
// A 
// B C
// C D E
// D E F G
// easier solution at pattern21.cpp
#include <iostream>
using namespace std;

int main()
{
   int n,i,j;
   
     cout << "n:" ;
     cin>> n ;
     for(i=1;i<=n;i++){
     for(j=1;j<=i;j++){
     char ch = 'A'+i +j-2;
     cout << ch << ' ';
     ch=ch+1;
     }
     cout << endl;
     }
}