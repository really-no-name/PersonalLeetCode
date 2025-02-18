/******************************************************************************
 * 文件名: 1732
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 找到最高海拔。
 * 时间复杂度： O(N)
 * 空间复杂度： O(N)
 * 执行用时： 3 ms
 * 消耗内存： 11.46 mb
 ******************************************************************************/


#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
  public:
    int largestAltitude(vector<int>& gain) {
      vector<int> altitude(gain.size() + 1, 0);
      for (int i = 0; i < gain.size(); i++) {
        altitude[i + 1] = gain[i] + altitude[i];
      }
      auto max_altitude = std::max_element(altitude.begin(), altitude.end());
      return *max_altitude;
    }
};


int main() {
  Solution s;
  vector<int> gain = {-5, 1, 5, 0, -7};
  cout << s.largestAltitude(gain) << endl;
}