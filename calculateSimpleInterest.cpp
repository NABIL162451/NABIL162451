#include <iostream>
using namespace std;

int main()
{
    double p,i,t,simpleinterestrate;

    cout << "principal ammount:";
    cin >> p;
    cout << " interest rate:";
    cin >> i;
    cout << "time:";
    cin >> t;
    simpleinterestrate = (p*i*t) / 100;
    cout << " simple interest rate:" << simpleinterestrate ;
    return 0;

}