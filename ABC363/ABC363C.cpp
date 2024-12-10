#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

bool isPalindrome(const string& str) {
    int len = str.size();
    for (int i = 0; i < len / 2; ++i) {
        if (str[i] != str[len - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;

    set<string> permutations;
    sort(S.begin(), S.end());
    do {
        permutations.insert(S);
    } while (next_permutation(S.begin(), S.end()));

    int ans = 0;
    for (const auto& P : permutations) {
        bool ok = true;
        for (int i = 0; i <= N - K; ++i) {
            string tmp = P.substr(i, K);
            if (isPalindrome(tmp)) {
                ok = false;
                break;
            }
        }
        if (ok) {
            ++ans;
        }
    }

    cout << ans << endl;
    return 0;
}