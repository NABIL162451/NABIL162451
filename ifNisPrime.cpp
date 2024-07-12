#include <iostream>
using namespace std;
int main()

{
    int n,i;
    bool isprime = true;  // initially n is prime
    cout << "n:";
    cin >> n ;
    if (n <=1)
    isprime = false; // just taking a name isprime.we can also write,  cout << "not prime".
    else{
        for( i=2;i<=n/2;i++){
            if ( n%i == 0)  // n is divisible by i,i on the right side cause i is smaller
            isprime= false;
            break;
    }}
    if(isprime){              //if isprime is true
    cout << "N is a prime Number";
    }
    else{
    cout <<" N is not a prime number";
    }
    return 0;
}