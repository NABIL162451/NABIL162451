// *****
// *****
// *****
// *****
// *****
// i is row and j is column      j=1 j=2 j=3
//                          i=1   *   *   *
//                          i=2   *   *   *
//                          i=3   *   *   *
// loop1 when i=1 for j=1 '*' for j=2 '*' for j=3 '*'
// loop2 when i=2 for j=1 '*' for j=2 '*' for j=3 '*'
// loop3 when i=3 for j=1 '*' for j=2 '*' for j=3 '*'




#include <iostream>
using namespace std;

int main()
{
    int n,i,j;
    cout << "input n: ";
    cin >> n;
    for(i=1;i<=n;i++)
    {
    for(j=1;j<=n;j++)
    {
        cout << '*'  ;
    }
    cout << endl;
    }
}