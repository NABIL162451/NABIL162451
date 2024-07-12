#include <iostream>
using namespace std;

int main()
{
    int n,i, fact=1;

    cout << " input n:";
     cin >> n;
    for (i=1; i<=n; i++)
    
    fact = i*fact;
    cout << "fact: " << fact;
}
