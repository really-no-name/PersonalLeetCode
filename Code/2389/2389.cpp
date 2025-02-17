/******************************************************************************
 * 文件名: 2389
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 和有限的最长子序列。
 * 时间复杂度：
 * 空间复杂度：
 * 执行用时：4 ms
 * 消耗内存：17.33 mb
 ******************************************************************************/


#include <iostream>
#include <vector>
#include <algorithm>  // 用于 sort 和 upper_bound

using namespace std;

class Solution {
public:
  vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
    // 对 nums 数组进行排序
    sort(nums.begin(), nums.end());

    // 计算前缀和
    for (size_t i = 1; i < nums.size(); i++) {
      nums[i] += nums[i - 1];
    }

    // 初始化结果数组
    vector<int> ans(queries.size(), 0);

    // 对于每个查询，使用二分查找找到满足条件的最大子序列长度
    for (size_t i = 0; i < queries.size(); i++) {
      // 使用 upper_bound 找到第一个大于 queries[i] 的位置
      auto it = upper_bound(nums.begin(), nums.end(), queries[i]);
      // 计算满足条件的子序列长度
      ans[i] = it - nums.begin();
    }

    return ans;
  }
};

int main() {
  Solution sol;

  // 测试用例 1
  vector<int> nums1 = {4, 5, 2, 1};
  vector<int> queries1 = {3, 10, 21};
  vector<int> result1 = sol.answerQueries(nums1, queries1);
  cout << "[";
  for (size_t i = 0; i < result1.size(); i++) {
    cout << result1[i];
    if (i < result1.size() - 1) {
      cout << ", ";
    }
  }
  cout << "]" << endl;  // 输出: [2, 3, 4]

  // 测试用例 2
  vector<int> nums2 = {2, 3, 4, 5};
  vector<int> queries2 = {1};
  vector<int> result2 = sol.answerQueries(nums2, queries2);
  cout << "[";
  for (size_t i = 0; i < result2.size(); i++) {
    cout << result2[i];
    if (i < result2.size() - 1) {
      cout << ", ";
    }
  }
  cout << "]" << endl;  // 输出: [0]

  return 0;
}