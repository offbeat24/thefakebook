#include <iostream>
using namespace std;

int main() {
  int c;
  int h, w, n;
  cin >> c;

  for(int i=0; i<c; i++) {
    cin >> h >> w >> n;

    int room;

    if (n%h == 0) room = h * 100 + (n/h);
    else room =  (n%h)* 100 + (n/h) + 1;

    cout << room << endl;

  }

} 