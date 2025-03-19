/******************************************************************************
 * 文件名: 2610
 * 作者: BOLUN XU
 * 创建日期: 2025
 * 版本: 1.0
 * 描述: 转换二维数组。
 * 时间复杂度： O(N^2)
 * 空间复杂度： O(N)
 ******************************************************************************/
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        vector<vector<int>> ans;
        unordered_map<int, int> cnt;

        // 统计每个元素的出现次数
        for (int num : nums) {
            cnt[num]++;
        }

        while (!cnt.empty()) {
            vector<int> row;
            for (auto& pair : cnt) {
                row.push_back(pair.first);
            }
            ans.push_back(row);

            // cnt 中的每个元素的出现次数都减一
            for (int x : row) {
                cnt[x]--;
                if (cnt[x] == 0) {
                    cnt.erase(x);
                }
            }
        }

        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 3, 4, 1, 2, 3, 1};
    vector<vector<int>> result = sol.findMatrix(nums);

    // 输出结果
    for (const auto& row : result) {
        for (int num : row) {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}