/******************************************************************************
 * 文件名: 1365
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 有多少小于当前数字的数字。
 * 时间复杂度： O(NLogN)
 * 空间复杂度： O(N)
 * 执行用时： 23 ms
 * 消耗内存： 13.89 mb
 ******************************************************************************/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end());

        // 输出排序后的数组
        // cout << "Debug: 排序后的 nums: ";
        for (int num : sorted_nums) {
            cout << num << " ";
        }
        cout << endl;

        vector<int> ans(nums.size(), 0);
        for (size_t i = 0; i < nums.size(); ++i) {
            // 输出当前查找的值
            // cout << "Debug: 当前查找: " << nums[i] << endl;

            // 使用 lower_bound 查找位置
            ans[i] = lower_bound(sorted_nums.begin(), sorted_nums.end(), nums[i]) - sorted_nums.begin();
        }

        return ans;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {8, 1, 2, 2, 3};
    vector<int> result = solution.smallerNumbersThanCurrent(nums);

    // 输出最终结果
    cout << "最终结果: ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}