// N:5
// 1
// 2 3
// 3 4 5
// 4 5 6 7
// 5 6 7 8 9
// each row start with its row value
#include <iostream>
using namespace std;
int main()
{
    int n,i,j;
    cout <<"N:";
    cin >>n;
    for(i=1;i<=n;i++)
    {
        int count = i;
    for(j=1;j<=i;j++)
    {
        cout << count << " " ;
        count=count+1;
    }
    cout << endl;
    }
}