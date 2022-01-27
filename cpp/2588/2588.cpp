#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a, b;
    int n = 3;
    int i, sum, tmp;
    sum = 0;
    cin >> a;
    cin >> b;
    for(i=0; i<n; i++) {
        tmp = a * (b%10);
        cout << tmp << endl;
        b= b/10;
        sum += tmp * pow(10,i);
    }
    cout << sum;
    return 0;
}