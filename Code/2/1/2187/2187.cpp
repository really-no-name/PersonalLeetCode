/******************************************************************************
 * 文件名: 2187
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 完成旅途的最少时间 —— 二分写法。
 * 时间复杂度： O(Nlogn)
 * 空间复杂度： O(1)
 * 执行用时： 85 ms
 * 消耗内存： 96.10 mb
 ******************************************************************************/
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
  long long minimumTime(vector<int>& time, int totalTrips) {
    long long left = 0;
    long long right = (long long)*max_element(time.begin(), time.end()) * totalTrips + 1;
    // cout << "Debug: Initial bound: " << left << ", " << right << endl;

    while (left < right) {
      long long mid = left + (right - left) / 2;
      long long total = 0;

      for (int t:time) {
        total += mid/t;
      }
      // cout << "Debug: At time " << mid << ", total finish " << total << "trips" << endl;

      if (total >= totalTrips) {
        right = mid;
      }
      else {
        left = mid + 1;
      }
      // cout << "Debug: New bound " << left << ", " << right << endl;
    }
    return right;
  }
};

int main() {
  Solution s;
  vector<int> time{1,2,3};
  cout << s.minimumTime(time, 5) << endl;
}