#include <iostream>

using namespace std;

int main(void)
{
    int n;
    int i;
    int j;
    int cnt = 0;
    int sum = 0;
    char ox[80];
    cin >> n;
    int score[n];
    for (i=0; i<n; i++) {
        cin >> ox;
        for (j=0; j<80; j++) {
            if (ox[j] == 'O') {
                cnt++;
                sum +=cnt;
            }
            else if (ox[j] == 'X') {
                cnt = 0;
            }
            else {
                cnt = 0;
                score[i] = sum;
                sum = 0;
                j=80;
            }
        }
    }
    for (i=0; i<n; i++) {
        cout << score[i] << '\n';
    }
    return 0;
}