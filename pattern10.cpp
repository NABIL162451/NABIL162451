// N:5
// 1
// 2 3
// 3 4 5
// 4 5 6 7
// 5 6 7 8 9
// each row start with its row value
// another method of patter 9 problem
#include <iostream>
using namespace std;
int main()
{
    int n,i,j;

    cout <<"N:";
    cin >>n;
    for(i=1;i<=n;i++)
    {
        
    for(j=0;j<i;j++) //accept j=1 we start form j=0 and do i+j 
    {
        cout << i+j << " " ;
    }
    cout << endl;
    }
}