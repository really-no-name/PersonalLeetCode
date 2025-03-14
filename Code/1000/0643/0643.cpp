/******************************************************************************
 * 文件名: 0643
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 。
 * 时间复杂度：
 * 空间复杂度：
 ******************************************************************************/
#include <iostream>
#include <algorithm>
#include <vector>
#include <float.h>

using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        float max_sum = - DBL_MAX;
        float sum = 0;
        for (int i = 0; i < nums.size(); i++) {
          sum += nums[i];
          if (i < k - 1) {
            continue;
          }
          max_sum = max(max_sum, sum);
          sum -= nums[i - k + 1];
        }
        return static_cast<double>(max_sum) / k;
    }
};

int main() {
  Solution s;
  vector<int> nums = {1, 12, -5, -6, 50, 3};
  cout << s.findMaxAverage(nums, 4) << endl;
}