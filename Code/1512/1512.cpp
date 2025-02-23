/******************************************************************************
 * 文件名: 1512
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 好数对的数目。
 * 时间复杂度： O(N ^2 )
 * 空间复杂度： O(1)
 ******************************************************************************/
#include <iostream>
#include <vector>

using namespace std;

class Solution {
  public:
    int numIdenticalPairs(vector<int>& nums) {
      int ans = 0;
      for (int i = 0; i < nums.size() - 1; ++i) {
        for (int j = i + 1; j < nums.size(); ++j) {
          if (nums[i] == nums[j]) {
            ++ans;
          }
        }
      }
      return ans;
    }
};

int main() {
  Solution s;
  vector<int> nums = {1, 2, 3, 1, 1, 3};
  cout << s.numIdenticalPairs(nums) << endl;
  return 0;
}
