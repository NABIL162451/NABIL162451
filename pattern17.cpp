// A 
// B C 
// D E F 
// G H I J 
// K L M N O 

#include <iostream>
using namespace std;

int main()
{
   int n,i,j;
   char ch = 'A';
    cout << "n:" ;
     cin>> n ;
     for(i=1;i<=n;i++){
     for(j=1;j<=i;j++){
     
     cout << ch << ' ';
     ch=ch+1;
     }
     cout << endl;
     }
}