// A B C D E 
// B C D E F
// C D E F G
// D E F G H
// E F G H I
// Easier way at pattern20.cpp to solve this problem
#include <iostream>
using namespace std;

int main()
{
    int i,j,n;
    cout <<"n:";
    cin >> n;
    for(i=1;i<=n;i++)
    {
    for(j=1;j<=n;j++)
    {
        char ch = 'A'+ i + j -2;  // like pattern 10 i+j-1 now if to get 1 MEANS TO GET i+j-1=1  i=1 and j=1.
                                //  now let's say 'A'=1 add A  NOW A+i+j-1= 1 so equation is A+i+j-2=ch
        cout << ch << ' ';
        ch =ch+1;
    }
    cout << endl;
}}