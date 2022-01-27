#include <iostream>

using namespace std;

int main(void)
{
    int num;
    int f_num;
    int s_num;
    int sum;
    int result = 0;
    int cnt = 0;

    cin >> num;

    if(num<10) num *= 10;

    result = num;

    while (1) {
        f_num = result / 10;
        s_num = result % 10;
        sum = f_num + s_num;
        result = (s_num*10) + (sum%10);
        cnt++;

        if(num == result) break;
    }
    cout << cnt;
    return 0;
}