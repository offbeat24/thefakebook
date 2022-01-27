#include <iostream>

using namespace std;

int main()
{
    int h, m;

    cin >> h >> m;

    m = m - 45;
    if (m >= 0) {
        cout << h << " " << m;
    }
    else {
        if (h == 0) {
            h = 23;  
            m = m + 60;
        } 
        else {
            h--;
            m = 60 + m;
        }
        cout << h << " " << m;
    }
    return 0;
}