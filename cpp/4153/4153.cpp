#include <iostream>
using namespace std;

int main() {
  int triangle[3];
  int tmp;
  while(1) {
    cin >> triangle[0] >> triangle[1] >> triangle[2];
    if (!triangle[0] && !triangle[1] && !triangle[2]) return 0;
    for(int i=0; i<2; i++){
      for(int j=i+1; j<3; j++){
        if(triangle[i]>triangle[j]) {
          tmp = triangle[i];
          triangle[i] = triangle[j];
          triangle[j] = tmp;
        }
      }
    }

    if((triangle[2]*triangle[2]) == (triangle[0]*triangle[0]) + (triangle[1]*triangle[1]) ) cout << "right" << endl;
    else cout << "wrong" << endl;
  }

} 