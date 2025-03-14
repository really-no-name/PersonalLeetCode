//
// Created by Bolun Xu.
// 0 ms, 13.47 mb

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
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
};

int main() {
    Solution s;
    vector<int> nums = {1,3,5,6};
    int target = 5;
    cout << s.searchInsert(nums, target) << endl;
}
