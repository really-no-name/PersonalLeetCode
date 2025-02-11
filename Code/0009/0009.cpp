//
// Created by Bolun Xu on 25-2-11.
// 11 ms, 10.67 mb
# include <iostream>
# include <string>
# include <algorithm>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        string rev_s = s;
        reverse(rev_s.begin(), rev_s.end());
        return s == rev_s;
    }
};

int main() {
    Solution s;
    int x = 123;
    bool result = s.isPalindrome(x);
    cout << (result ? "true" : "false") << endl;
    return 0;
}