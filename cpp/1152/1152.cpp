#include <iostream>
#include <string>
using namespace std;
int main(void) {
    string sent;
    getline(cin, sent);
    int cnt = 1;
    for(int i = 0; i<sent.length(); i++) {
        if (sent[i] == ' ') cnt++;
    }
    if(sent[0] == ' ') cnt--;
    if(sent[sent.length()-1] == ' ') cnt--;
    cout << cnt;
}