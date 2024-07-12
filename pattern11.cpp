// N:5
// 1 
// 2 1
// 3 2 1
// 4 3 2 1
// 5 4 3 2 1

#include <iostream>
using namespace std;
int main()
{
    int n,i,j;

    cout <<"N:";
    cin >>n;
    for(i=1;i<=n;i++)
    {
        
    for(j=0;j<i;j++) //accept j=1 we start form j=0 and do i+j 
    {
        cout << i-j << " " ;
    }
    // Or we can do it like this
    // for(j=1;j<=i;j++) //accept j=1 we start form j=0 and do i+j 
    // {
    //     cout << i-j+1 << " " ;
    // }
    cout << endl;
    }
}