/******************************************************************************
 * 文件名: 2529
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 正整数和负整数的最大计数。
 * 时间复杂度：O(N)
 * 空间复杂度：O(1)
 * 执行用时：0 ms
 * 消耗内存：20.99 mb
 ******************************************************************************/


#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
  private:
    int lower_bound(vector<int>& nums, int target) {
      int left = 0, right = nums.size();
      while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) {
          left = mid + 1;
        }
        else {
          right = mid;
        }
      }
      return left;
    }

  public:
    int maximumCount(vector<int>& nums) {
      int negative = lower_bound(nums, 0);
      int positive = nums.size() - lower_bound(nums, 1);
      return max(negative, positive);
    }
};

int main() {
  Solution s;
  vector<int> nums1 = {-2,-1,-1,1,2,3};
  vector<int> nums2 = {-3,-2,-1,0,0,1,2};
  vector<int> nums3 = {5,20,66,1314};
  cout << s.maximumCount(nums1) << endl;
  cout << s.maximumCount(nums2) << endl;
  cout << s.maximumCount(nums3) << endl;
  return 0;
}