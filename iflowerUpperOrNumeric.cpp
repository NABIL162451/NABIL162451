#include <iostream>
using namespace std;

int main()
{
    char ch;
    cout << "Input the character a-z or A-Z OR 1-9: ";
    cin >> ch;
    if (ch >= 'a' && ch <= 'z')
    cout << "Lowercase";
    else if (ch >= 'A' && ch <= 'Z' )
    cout << "Uppercase";
    else if (ch >= '0'&& ch <= '9' )
    cout << "Numeric" ;
    else
    cout <<" Nothing";

}