/******************************************************************************
 * 文件名: Code
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 。
 * 时间复杂度：
 * 空间复杂度：
 * 执行用时：
 * 消耗内存：
 ******************************************************************************/


class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
      int left = 0;
      int right = arr.size() - 1;
      while (left < right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] > arr[mid + 1]) {
          right = mid;
        }
        else {
          left = mid + 1;
        }
      }
      return right;
    }
};