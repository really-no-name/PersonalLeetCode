// Bolun Xu
// 3ms, 8.91 mb

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length();
        int n = p.length();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        dp[0][0] = true;  // 空字符串和空模式匹配

        // 处理模式中的 '*'，初始化 dp[0][j]
        for (int j = 2; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }

        // 填充 dp 表
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == '*') {
                    // 两种情况：
                    // 1. '*' 匹配零个前面的元素（即忽略 '*' 和它前面的字符）
                    // 2. '*' 匹配一个或多个前面的元素（即当前字符与模式的前一个字符匹配）
                    dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'));
                } else {
                    // 当前字符匹配，且前面的字符也匹配
                    dp[i][j] = dp[i - 1][j - 1] && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
                }
            }
        }

        return dp[m][n];
    }
};

int main() {
    Solution sol;
    cout << boolalpha;  // 输出 bool 值为 true/false
    cout << sol.isMatch("aa", "a") << endl;       // 输出: false
    cout << sol.isMatch("aa", "a*") << endl;      // 输出: true
    cout << sol.isMatch("ab", ".*") << endl;      // 输出: true
    cout << sol.isMatch("aab", "c*a*b") << endl;  // 输出: true
    cout << sol.isMatch("mississippi", "mis*is*p*.") << endl;  // 输出: false
    return 0;
}