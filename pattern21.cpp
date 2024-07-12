// n:4
// A 
// B C
// C D E
// D E F G
// easier solution of pattern18.cpp
#include <iostream>
using namespace std;

int main()
{
   int n,i,j;
   
     cout << "n:" ;
     cin>> n ;
     for(i=1;i<=n;i++){
        char ch = 'A' +i -1;
     for(j=1;j<=i;j++){
     cout << ch << ' ';
     ch=ch+1;
     }
     cout << endl;
     }
}