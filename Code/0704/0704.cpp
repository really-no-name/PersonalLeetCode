/******************************************************************************
 * 文件名: 0704
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 二分查找。
 * 时间复杂度：O(LogN)
 * 空间复杂度：O(1)
 * 执行用时：0 ms
 * 消耗内存：30.66 mb
 ******************************************************************************/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // if (nums.empty() || target < nums[0] || target > nums[nums.size() - 1]) return -1;

        int left = 0, right = nums.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            }
            else if (nums[mid] > target) {
                right = mid - 1;
            }
            else if (nums[mid] == target) {
                return mid;
            }
        }
        return -1;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {-1,0,3,5,9,12};
    int target = 2;
    cout << sol.search(nums, target) << endl;
    return 0;
}
