#include <iostream>

using namespace std;

int main(void)
{
    int c;
    cin >> c;
    int n;
    int i, j;
    double pct[c];
    for (i=0; i<c; i++) {
        cin >> n;
        int score[n];
        int sum = 0;
        int cnt = 0;
        for (j=0; j<n; j++) {
            cin >> score[j];
            sum += score[j];
        }
        sum /= n;
        for (j=0; j<n; j++) {
            if (score[j] > sum) cnt++;
        }
        pct[i] = (double)cnt/n * 100;
    
        cout << fixed;
        cout.precision(3);
        cout << pct[i] << '%' << '\n';
    }
    return 0;
}