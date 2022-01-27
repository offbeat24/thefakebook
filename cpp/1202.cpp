#include <iostream>

using namespace std;

int main()
{
    int n, k;
    int mv[1000000][2];
    int c[100000000];
    //priority_queue &heap  해야해
    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
        cin >> mv[i][0] >> mv[i][1];
    }
    for (int i = 0; i < k; i++)
    {
        cin >> c[i];
    }
}