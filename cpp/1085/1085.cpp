#include <iostream>
using namespace std;

int main()
{
    int x, y, w, h;

    cin >> x >> y >> w >> h;

    int xmin = (x < (w - x)) ? x : (w - x);
    int ymin = (y < (h - y)) ? y : (h - y);

    cout << ((xmin < ymin) ? xmin : ymin);
}