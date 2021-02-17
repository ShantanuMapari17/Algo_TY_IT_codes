#include<iostream>
using namespace std;
int main()
{
    long long int n;
    cin>>n;
    int count=0;
    while(n){
        if(n%2==0)
            n=n/2;
        else
            n--;
        count++;
    }
    cout<<count;
}