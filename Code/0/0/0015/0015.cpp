//
// Created by Bolun Xu on 25-2-11.
// 43 ms, 28.63 mb
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());  // 排序
        vector<vector<int>> ans;

        for (int i = 0; i < nums.size() - 2; i++) {
            int x = nums[i];
            if (i > 0 && x == nums[i - 1]) {  // 跳过重复的 i
                continue;
            }
            // 优化
            if (x + nums[i + 1] + nums[i + 2] > 0) {
                break;
            }
            if (x + nums[nums.size() - 2] + nums[nums.size() - 1] < 0) {
                continue;
            }

            int j = i + 1;
            int k = nums.size() - 1;
            while (j < k) {
                int sum = x + nums[j] + nums[k];
                if (sum > 0) {
                    k--;
                } else if (sum < 0) {
                    j++;
                } else {
                    ans.push_back({x, nums[j], nums[k]});
                    j++;
                    while (j < k && nums[j] == nums[j - 1]) {  // 跳过重复的 j
                        j++;
                    }
                    k--;
                    while (j < k && nums[k] == nums[k + 1]) {  // 跳过重复的 k
                        k--;
                    }
                }
            }
        }

        return ans;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> result = solution.threeSum(nums);

    // 输出结果
    cout << "[";
    for (int i = 0; i < result.size(); i++) {
        cout << "[";
        for (int j = 0; j < result[i].size(); j++) {
            cout << result[i][j];
            if (j < result[i].size() - 1) {
                cout << ", ";
            }
        }
        cout << "]";
        if (i < result.size() - 1) {
            cout << ", ";
        }
    }
    cout << "]" << endl;

    return 0;
}