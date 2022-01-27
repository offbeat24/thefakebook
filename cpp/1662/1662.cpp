#include <iostream>
#include <string>
#include <cstdlib>
#include <cctype>
using namespace std;

string str;
int tmp = 0;
int dat = 0;
int flag = 0;

void zip(int p) {
    for(int i=p; i >= 0; i--) {
        if (isdigit(str[i]) != 0) {
            tmp ++;
        }else if (str[i] == '(') {
            int a = str[i-1] -'0';
            tmp *= a;
            flag = i-1;
            return;
        }else if (str[i] == ')') {
            dat += tmp;
            tmp = 0;
            zip(i-1);
            i = flag;
        }
    }
    tmp += dat;
    return;
}
int main() {

    cin >> str;
    zip(str.length()-1);
    cout << tmp;

    return 0;
}
