#include <iostream>
using namespace std;
int d(int n) {
    if(n < 10) {
        return n*2;
    }
    else if (n < 100) {
        return n+(n/10)+(n%10);
    }
    else if (n < 1000) {
        return n+(n/100)+((n%100)/10)+(n%10);
    }
    else {
        return n+(n/1000)+((n%1000)/100)+((n%100)/10)+(n%10);
    }
}
int main(void) {
    bool num[10035] = {false};
    for (int i=1; i<=10000; i++) {
        num[d(i)] = true;
    }
    for (int i=1; i<=10000; i++) {
        if (!num[i]) cout << i << '\n';
    }
    return 0;
}