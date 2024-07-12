n:5
    1
   121
  12321
 1234321
123454321

#include <iostream>
using namespace std;

int main()
{
   int n,i,j,k,l;
     cout << "n:" ;
     cin>> n ;
     for(i=1;i<=n;i++)
     {  
        int count = 1;
        //print space
        for(j=1;j<=n-i;j++)
        { 
        
        cout << " ";
        }
        for(k=1;k<=i;k++)
        {
        cout << count;
        count=count+1;  
     }
     for(l=1;l<=i-1;l++){
     cout << count-2;
     count =count-1;
     }
        
     cout << endl;
     }
}