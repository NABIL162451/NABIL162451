#include <iostream>
using namespace std;

int main()
{
    int n,i, sum=0;

    cout << " input n:";
     cin >> n;
    for (i=0; i<=n; i++)
    if ( i % 2 == 1)
    sum = i+sum;
    cout << "sum: " << sum;
}
