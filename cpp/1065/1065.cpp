#include <iostream>

using namespace std;
bool hansu(int n) {
    if (n<100) return 1;
    else if (n<1000) {
        if(((n/100)-((n%100)/10)) == ((((n%100)/10)) - (n%10))) return 1;
        else return 0;
    }
    else return 0;
}
int main(void) {
    int n;
    cin >> n;
    int cnt=0;
    for(int i=1; i<=n; i++) {
        if(hansu(i)) cnt++;
    }
    cout << cnt;
    return 0;
}