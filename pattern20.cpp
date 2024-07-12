// A B C D E 
// B C D E F
// C D E F G
// D E F G H
// E F G H I
// easier solution of pattern16.cpp
#include <iostream>
using namespace std;

int main()
{
    int i,j,n;
    cout <<"n:";
    cin >> n;
    for(i=1;i<=n;i++)
    {
        char ch= 'A'+ i-1;
    for(j=1;j<=n;j++)
    {                    
        cout << ch << ' ';
        ch =ch+1;
    }
    cout << endl;
}}