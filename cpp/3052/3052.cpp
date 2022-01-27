#include <iostream>

using namespace std;

int main(void)
{
    int num[10];
    int cnt[42] = {0};
    int r = 0;
    int i;
    for (i=0;i<10;i++) cin >> num[i];
    for (i=0;i<10;i++) {
        cnt[num[i]%42]++;
    }
    for (i=0;i<42;i++) {
        if(cnt[i]!=0) r++;
    }
    cout << r;
    return 0;
}