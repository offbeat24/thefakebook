#include <iostream>

using namespace std;

int main(void)
{
    int n, x;
    cin >> n >> x;

    int a[n], i;
    for(i=0; i<n; i++) {
        cin >> a[i];
    }
    for(i=0; i<n; i++) {
        if(a[i] < x) cout << a[i] << " ";
    }
}