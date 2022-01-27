#include <iostream>

using namespace std;

int main(void)
{
    int num;
    int max = 0;
    int i, tmp;
    for(i=0; i<9; i++) {
        cin >> num;
        if(num > max) {
            max = num;
            tmp = i+1;
        }
    }
    
    cout << max << '\n' << tmp;
    return 0;
}