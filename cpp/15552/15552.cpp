#include <iostream>

using namespace std;

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int t;
    int i;
    int a, b;
    cin >> t;
    for(i=0; i<t; i++) {
        cin >> a >> b;
        cout << a+b <<'\n';
    }
}