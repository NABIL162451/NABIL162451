// 1 2 3 
// 4 5 6
// 7 8 9

#include <iostream>
using namespace std;
int main()
{
    int n,i,j;
    int count=1;
    cout <<"N:";
    cin >>n;
    for(i=1;i<=n;i++)
    {
    for(j=1;j<=n;j++)
    {
        cout << count << " ";
        count=count+1;
    }
    cout << endl;
    }
}