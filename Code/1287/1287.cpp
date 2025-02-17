/******************************************************************************
 * 文件名: 1287
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 有序数组中出现次数超过25%的元素。
 * 时间复杂度：O(NLogN)
 * 空间复杂度：O(1)
 * 执行用时：3 ms
 * 消耗内存：16.17 mb
 ******************************************************************************/
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int size = arr.size();
        for (int i = 1; i < size; i++) {
          // int left = arr.begin() + i;
          auto right = upper_bound(arr.begin(), arr.end(), arr[i]);
          int length = right - (arr.begin() + i);
          if (length > 0.25 * size) {
              return arr[i];
          }
        }
        return arr[0];
    }
};

int main() {
  Solution s;
  vector<int> arr = {1, 2, 2, 6, 6, 6, 6, 7, 10};
  cout << s.findSpecialInteger(arr) << endl;
}