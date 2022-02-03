#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
  string strnum1, strnum2;
  int num1, num2;
  cin >> strnum1 >> strnum2;
  reverse(strnum1.begin(),strnum1.end());
  num1 = stoi(strnum1);
  reverse(strnum2.begin(),strnum2.end());
  num2 = stoi(strnum2);

  cout << ((num1 > num2) ? num1 : num2);
} 