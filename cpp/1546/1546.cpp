#include <iostream>

using namespace std;

int main(void)
{
    int n;
    cin >> n;
    int score[n];
    int i;
    double avg = 0;
    int max=0;
    for (i=0;i<n;i++) {
        cin >> score[i];
        if(score[i] > max) max = score[i];
        avg += score[i];
    }
    avg = (avg / max * 100) / n;
    cout << fixed;
    cout.precision(6);
    cout << avg << endl;
}