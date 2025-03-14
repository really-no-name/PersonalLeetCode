/******************************************************************************
 * 文件名: 1456
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 定长子串中元音的最大数目。
 * 时间复杂度： O(N)
 * 空间复杂度： O(1)
 * 执行用时： 3 ms
 * 消耗内存： 13.00 mb
 ******************************************************************************/
#include <iostream>

using namespace std;

class Solution {
public:
  int maxVowels(string s, int k) {
    int ans = 0;
    int vow = 0;
    for (int i = 0; i < s.length(); i++) {
      // 进入窗口
      // cout << "DEBUG: ----------------------------------------" << endl;
      // cout << "DEBUG: s[" << i << "]= " << s[i] << " 进入窗口" << endl;
      if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
        // cout << "DEBUG: s[" << i << "]= " << s[i] << " 是元音" << endl;
        vow++;
      }
      if (i < k - 1) {
        // cout << "DEBUG: 滑窗长度不满足" << endl;
        continue;
      }
      // 更新答案
      // cout << "DEBUG: 当前滑窗内元音数为 " << vow << endl;
      ans = max(ans, vow);
      // 离开窗口
      // cout << "DEBUG: s[" << i - k + 1 << "]= " << s[i - k + 1] << "离开窗口" << endl;
      if (s[i - k + 1] == 'a' || s[i - k + 1] == 'e' || s[i - k + 1] == 'i' || s[i - k + 1] == 'o' || s[i - k + 1] == 'u') {
        // cout << "DEBUG: s[" << i - k + 1 << "]= " << s[i - k + 1] << " 是元音" << endl;
        vow--;
      }
    }
    return ans;
  }
};

int main() {
  Solution s;
  cout << s.maxVowels("abciiidef", 3) << endl;
}