#include<iostream>
#include<math.h>
using namespace std;
bool isSquare(long long int x){
    long long int y=sqrt(x);
    return (y*y==x);
}

int main()
{
    long int n;
    cin>>n;
    long int count=0;
    while(n){
        long long int area;
        cin>>area;
        if(isSquare(area)){
            // cout<<area<<endl;
            count++;
        }
            
        n--;
    }
    cout<<count;
}