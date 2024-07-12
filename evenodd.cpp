#include <iostream>
using namespace std;

int main()
{
    int n;

    cout << "n:";
    cin >> n;

    if (n % 2 == 0)
    {
    cout << "n is a even number";
    }
    else if ( n % 2 == 1)
    {
    cout << "n is a odd number";
    }
     else{
        cout << " n is not a number";
     }
    return 0;
}
