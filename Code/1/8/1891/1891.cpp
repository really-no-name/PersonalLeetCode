/******************************************************************************
 * 文件名: 1891
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 割绳子。
 * 时间复杂度：
 * 空间复杂度：
 ******************************************************************************/
#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
  int maxLength(vector<int>& ribbons, int k) {
    long long total = accumulate(ribbons.begin(), ribbons.end(), 0LL);
    if (k > total) return 0;
    if (k == total) return 1;

    auto check = [&](int x) {
      int s = 0;
      for (int ribbon : ribbons) {
        s += ribbon / x;
      }
      return s >= k;
    };

    int left = 0;
    int right = *max_element(ribbons.begin(), ribbons.end());
    while (left + 1 < right) {
      int mid = left + (right - left) / 2;
      if (check(mid)) {
        left = mid;
      }
      else {
        right = mid;
      }
    }
    return left;
  }
};


int main() {
  vector<int> ribbons = {9, 7, 5};
  cout << Solution().maxLength(ribbons, 3) << endl;
}