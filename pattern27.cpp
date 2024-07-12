// 12345
//  2345
//   345
//    45
//     5
#include <iostream>
using namespace std;

int main()
{
   int n,i,j,k;
     cout << "n:" ;
     cin>> n ;
     for(i=1;i<=n;i++)
     {  
        int count = i;
        //print space
        for(j=1;j<=i-1;j++)
        { 
        
        cout << " ";
        }
        for(k=1;k<=n-i+1;k++)
        {
        cout << count;
        count =count+1;
     }
   
     cout << endl;
     }
}