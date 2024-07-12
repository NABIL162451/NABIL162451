// 54321
// 54321
// 54321
// 54321
// 54321

#include <iostream>
using namespace std;
int main()
{
    int n,i,j;
    cout <<"N:";
    cin >>n;
    for(i=1;i<=n;i++)
    {
    for(j=1;j<=n;j++)
    {
        cout << n-j+1;
    }
    cout << endl;
    }
}