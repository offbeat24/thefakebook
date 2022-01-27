#include <iostream>

using namespace std;

int main(void)
{
    int a, b, c;
    int cnt[10] = {0};
    int rslt = 0;
    cin >> a >> b >> c;
    rslt = a*b*c;
    int i;
    while(rslt>0) {
        cnt[rslt%10]++;
        rslt = rslt / 10;
    }
    for (i=0; i<10; i++) cout << cnt[i] << '\n';
    return 0;
}