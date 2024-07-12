// N:5
// A 
// B B 
// C C C 
// D D D D 
// E E E E E

#include <iostream>
using namespace std;
int main()
{
    int n,i,j;
    cout <<"N:";
    cin >>n;
    for(i=1;i<=n;i++)
    {
        
    for(j=1;j<=i;j++) //accept j=1 we start form j=0 and do i+j 
    {
        char ch='A'+i-1 ; 
        cout << ch << " " ;
    }
    cout << endl;
    }
}