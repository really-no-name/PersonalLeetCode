#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    int lower_bound(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return left;
    }

public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = lower_bound(nums, target);
        if (start == nums.size() || nums[start] != target) {
            return {-1, -1};
        }
        int end = lower_bound(nums, target + 1) - 1;
        return {start, end};
    }
};

int main() {
    Solution solution;
    vector<int> nums = {5, 7, 7, 8, 8, 10};
    int target = 8;

    vector<int> result = solution.searchRange(nums, target);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;  // 输出: [3, 4]

    return 0;
}