#include<iostream>
using namespace std;
int main()
{
    cout<<"Enter a num: ";
    int num;
    cin>>num;
    if(num%5==0 && num%7==0)
        cout<<"Hello World\n";
    else if(num%5==0)
        cout<<"Hello"<<endl;
    else if(num%7==0)
        cout<<"World"<<endl;
    return 0;
}