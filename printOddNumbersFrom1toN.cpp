#include <iostream>
using namespace std;

int main()
{
    int n,i;

    cout << " input n:";
     cin >> n;
     cout << " odd numbers: ";
    for (i=0; i<=n; i++)
     if (i%2==1)
    cout << i <<" ";
}