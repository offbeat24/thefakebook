#include <iostream>

using namespace std;

int main() {
  string input;

  getline(cin,input);

  string asc = "1 2 3 4 5 6 7 8";
  string des = "8 7 6 5 4 3 2 1";

  if (!input.compare(asc)) cout << "ascending";
  else if (!input.compare(des)) cout << "descending";
  else cout << "mixed";
} 