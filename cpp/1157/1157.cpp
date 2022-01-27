#include <iostream>
#include <string>
using namespace std;
int main(void) {
    string word;
    cin >> word;
    int alpha[26] = {0, };
    int max = 0;
    int cnt = 0;
    int tmp;
    for(int i=0; i<word.length(); i++) {
        if(word[i] >= 'a') word[i] -= 32;
        alpha[word[i]-'A']++;
    }
    for(int i = 0; i<26; i++) {
        if (max < alpha[i])
        {
            max = alpha[i];
            cnt = 0;
            tmp = i;
        }
        if (max == alpha[i]) cnt ++;
    }
    if (cnt > 1) cout << "?";
    else cout << (char)(tmp+'A');

    return 0;
}