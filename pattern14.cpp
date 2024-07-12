// A B C D 
// A B C D
// A B C D
// A B C D

#include <iostream>
using namespace std;
int main()
{
    int n,i,j;
    cout <<"N:";
    cin >>n;
    for(i=1;i<=n;i++)
    {
        
    for(j=1;j<=n;j++) //accept j=1 we start form j=0 and do i+j 
    {
        char ch='A'+j-1 ;     // A=65 SO 65+(j=2)-1 = 66 WHICH IS THE ASCII VALUE OF B if 67 is the ASCII value of C just like this 
        cout << ch << " " ;
    }
    cout << endl;
    }
}