#include <iostream>
#include <string>
using namespace std;
int main(void) {
    string s;
    string alpha = "abcdefghijklmnopqrstuvwxyz";
    cin >> s;
    for (int i=0; i<alpha.length(); i++) {
        cout << (int)s.find(alpha[i]) << " ";
    }
}