/******************************************************************************
 * 文件名: Code
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 重新排列数组。
 * 时间复杂度： O(N)
 * 空间复杂度： O(N)
 * 执行用时： 0 ms
 * 消耗内存： 13.52 mb
 ******************************************************************************/
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> shuffle(vector<int>& nums, int n) {
    vector<int> x(nums.begin(), nums.begin() + n);
    vector<int> y(nums.begin() + n, nums.end());
    vector<int> ans;
    for (int i = 0; i < n; i++) {
      ans.push_back(x[i]);
      ans.push_back(y[i]);
    }
    return ans;
  }
};

int main() {
  Solution s;
  vector<int> nums = {2, 5, 1, 3, 4, 7};
  int  n = 3;
  vector<int> ans = s.shuffle(nums, n);
  for (int num: ans) {
    cout << num << ' ';
  }
  cout << endl;
  return 0;
}