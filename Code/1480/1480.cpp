/******************************************************************************
 * 文件名: 1480
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 一维数组的动态和。
 * 时间复杂度： O(N)
 * 空间复杂度： O(1)
 * 执行用时： 0 ms
 * 消耗内存： 12.32 mb
 ******************************************************************************/
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> runningSum(vector<int>& nums) {
    for (int i = 1; i < nums.size(); i++) {
      nums[i] += nums[i-1];
    }
    return nums;
  }
};

int main() {
  Solution s;
  vector<int> nums = {1,2,3,4};
  vector<int> result = s.runningSum(nums);
  cout << "最终结果: ";
  for (int num : result) {
    cout << num << " ";
  }
  cout << endl;
  return 0;
}