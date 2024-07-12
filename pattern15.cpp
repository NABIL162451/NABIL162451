// N:4
// A B C D 
// E F G H
// I J K L
// M N O P

#include <iostream>
using namespace std;
int main()
{
    int n,i,j;
    char ch ='A' ;
    cout <<"N:";
    cin >>n;
    for(i=1;i<=n;i++)
    {       
    for(j=1;j<=n;j++) //accept j=1 we start form j=0 and do i+j 
    {
        
        cout << ch << " " ;
        ch = ch+1;
    }
    cout << endl;
    }
}