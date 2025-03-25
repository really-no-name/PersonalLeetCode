/******************************************************************************
 * 文件名: 0011
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 盛最多水的容器。
 * 时间复杂度： O(N)
 * 空间复杂度： O(1)
 ******************************************************************************/
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
  int maxArea(vector<int>& height) {
    int left = 0;
    int right = height.size() - 1;
    int max_area = 0;
    while (left < right) {
      if (height[left] < height[right]) {
        int area = height[left] * (right - left);
        max_area = max(max_area, area);
        left++;
      }
      else {
        int area = height[right] * (right - left);
        max_area = max(max_area, area);
        right--;
      }
    }
    return max_area;
  }
};

int main() {
  Solution solution;
  vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
  cout << solution.maxArea(height) << endl;
}