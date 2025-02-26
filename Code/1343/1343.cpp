/******************************************************************************
 * 文件名: 1343
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 大小为 K 且平均值大于等于阈值的子数组数目。
 * 时间复杂度： O(N)
 * 空间复杂度： O(1)
 ******************************************************************************/
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int numOfSubarrays(vector<int>& arr, int k, int threshold) {
    threshold = threshold * k;
    int sum = 0;
    int ans = 0;
    for (int i = 0; i < arr.size(); i++) {
      sum += arr[i];
      if (i < k - 1) {
        continue;
      }
      if (sum >= threshold) {
        ans++;
      }
      sum -= arr[i - k + 1];
    }
    return ans;
  }
};

int main() {
  Solution s;
  vector<int> arr = {2,2,2,2,5,5,5,8};
  cout << s.numOfSubarrays(arr, 3, 4) << endl;
}