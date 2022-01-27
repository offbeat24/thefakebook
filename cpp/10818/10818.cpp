#include <iostream>

using namespace std;

int main(void)
{
    int n;
    cin >> n;
    int num[n];
    int min = 1000000;
    int max = -1000000;
    int i;
    for(i=0; i<n; i++) {
        cin >> num[i];
    }
    for (i=0; i<n; i++) {
        if(num[i] < min) min = num[i];
        if(num[i] > max) max = num[i];
    }
    cout << min << " " << max;
    return 0;
}