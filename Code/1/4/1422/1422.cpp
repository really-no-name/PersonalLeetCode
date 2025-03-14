/******************************************************************************
 * 文件名: Code
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 分割字符串的最大得分。
 * 时间复杂度： O(N)
 * 空间复杂度： O(1)
 * 执行用时： 3 ms
 * 消耗内存： 8.72 mb
 ******************************************************************************/
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxScore(string s) {
        int left0 = 0;
        int right1 = ranges::count(s, '1');
        int ans = 0;
        for (int i = 0; i + 1 < s.length(); i++) {
          if (s[i] == '0') {
            left0 ++;
          }
          else {
            right1 --;
          }
          ans = max(ans, left0 + right1);
        }
        return ans;
    }
};

int main() {
  Solution s;
  cout << s.maxScore("011101") << endl;
}