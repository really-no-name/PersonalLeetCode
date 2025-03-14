/******************************************************************************
 * 文件名: 1004
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 最大连续1的个数 III。
 * 时间复杂度:  O(N)
 * 空间复杂度： O(N)
 ******************************************************************************/
#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
  public:
    int longestOnes(vector<int>& nums, int k) {
      /*
      :param nums: 二进制数组 nums
      :param k: 整数
      :return: 假设最多可以翻转 k 个 0 ，则返回执行操作后 数组中连续 1 的最大个数
      */
      int ans = 0;
      int left = 0;
      unordered_map<int, int> cnt;
      for (int right = 0; right < nums.size(); ++right) {
        ++cnt[nums[right]];

        while (cnt[0] > k) {
          --cnt[nums[left]];
          left++;
        }

        ans = max(ans, right - left + 1);
      }
      return ans;
    }
};

int main() {
  Solution s;
  vector<int> nums = {0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1};
  int k = 3;
  cout << s.longestOnes(nums, k) << endl; // 输出结果
  return 0;
}