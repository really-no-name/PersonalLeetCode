/******************************************************************************
 * 文件名: 1534
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 。
 * 时间复杂度：
 * 空间复杂度：
 ******************************************************************************/
#include <iostream>
#include <vector>
#include <cmath> // for abs function

using namespace std;

class Solution {
public:
  int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
    int ans = 0;
    int n = arr.size();
    for (int i = 0; i < n - 2; ++i) {
      for (int j = i + 1; j < n - 1; ++j) {
        if (abs(arr[i] - arr[j]) <= a) {
          for (int k = j + 1; k < n; ++k) {
            if (abs(arr[j] - arr[k]) <= b && abs(arr[i] - arr[k]) <= c) {
              ans++;
            }
          }
        }
      }
    }
    return ans;
  }
};

int main() {
  Solution sol;
  vector<int> arr = {3, 0, 1, 1, 9, 7};
  int a = 7, b = 2, c = 3;
  cout << sol.countGoodTriplets(arr, a, b, c) << endl; // Output: 4
  return 0;
}