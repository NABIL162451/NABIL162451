 #include <iostream>
 using namespace std;
  int main()
  {
    int a,b,c;
    cout << "a:";
    cin >>a;
    cout << "b:";
    cin >>b;
    cout << "c:";
    cin >>c;

    if (a+b>c && b+c>a && c+a>b)
    {
    cout <<" valid traingle";
    }
    else{
    cout << " not valid traingle";
    }
    return 0;
    
  }
