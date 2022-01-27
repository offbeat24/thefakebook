#include <iostream>
using namespace std;
int main()
{
    int n = 0, goal = 0, my = 0;
    cin >> n >> goal;
    int card[100];
    for (int i = 0; i < n; i++)
        cin >> card[i];

    int tmp;

    for (int i = 0; i < n - 1; i++)
    {
        if (card[i] > card[i + 1])
        {
            tmp = card[i];
            card[i] = card[i + 1];
            card[i + 1] = tmp;
        }
    }
    
    for (int i = 0; i < n-2; i ++) {
        for (int j = i+1; j<n-1; j ++) {
            for (int k = j +1; k<n; k ++){
                tmp = card[i] + card[j] + card[k];
                if (tmp <= goal) {
                    if(tmp > my) my = tmp;
                }
            }
        }
    }

    cout << my;
}