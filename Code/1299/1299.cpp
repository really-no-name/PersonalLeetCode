/******************************************************************************
 * 文件名: 1299
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 将每个元素替换为右侧最大元素。
 * 时间复杂度：O(N)
 * 空间复杂度：O(N)
 * 执行用时：5 ms
 * 消耗内存：71.19 mb
 ******************************************************************************/


#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
  public:
    vector<int> replaceElements(vector<int>& arr) {
      int max_value = -1;
      vector<int> ans(arr.size(), -1);
      for (int i = arr.size() - 1; i >= 0; i--) {
        int x = arr[i];
        ans[i] = max_value;
        max_value = max(max_value, x);
      }
      return ans;

    }
};


int main() {
  Solution s;
  vector<int> arr1 = {17, 18, 5, 4, 6, 1};
  vector<int> result1 = s.replaceElements(arr1);
  cout << "[";
  for (size_t i = 0; i < result1.size(); i++) {
    cout << result1[i];
    if (i < result1.size() - 1) {
      cout << ", ";
    }
  }
  cout << "]" << endl;
  return 0;
}